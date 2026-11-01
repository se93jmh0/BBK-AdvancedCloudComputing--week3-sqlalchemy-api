import pytest

from fastapi.testclient import TestClient


COURSE = {"code": "CC101", "title": "Cloud Computing", "lecturer": "Alex"}


def test_create_and_retrieve(client):
    created = client.post("/courses", json=COURSE)
    assert created.status_code == 201
    body = created.json()
    assert body == {"id": body["id"], **COURSE}
    assert isinstance(body["id"], int)
    fetched = client.get(f"/courses/{body['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == body
    assert client.get("/courses").json() == [body]


def test_duplicate_does_not_add_row(client):
    assert client.post("/courses", json=COURSE).status_code == 201
    duplicate = client.post("/courses", json=COURSE)
    assert duplicate.status_code == 409
    assert duplicate.json()["detail"] == "Course code already exists"
    assert len(client.get("/courses").json()) == 1


def test_invalid_input_does_not_add_row(client):
    response = client.post("/courses", json={**COURSE, "code": "X"})
    assert response.status_code == 422
    assert any(error["loc"] == ["body", "code"] for error in response.json()["detail"])
    assert client.get("/courses").json() == []


def test_missing_course(client):
    response = client.get("/courses/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Course not found"}


def test_starts_empty(client):
    # This remains true even when other tests have created courses.
    assert client.get("/courses").json() == []


def test_data_survives_new_application(app_factory):
    with TestClient(app_factory()) as first:
        created = first.post("/courses", json=COURSE)
        assert created.status_code == 201
        body = created.json()
    # A second app and new sessions use the same file within this test.
    with TestClient(app_factory()) as restarted:
        assert restarted.get(f"/courses/{body['id']}").json() == body


def test_missing_title(client):
    courses_missing_title = {k: v for k, v in COURSE.items() if k != "title"}
    response = client.post("/courses", json=courses_missing_title)
    assert response.status_code == 422
    assert any(error["loc"] == ["body", "title"] for error in response.json()["detail"])
    assert client.get("/courses").json() == []


def test_valid_then_invalid_then_valid(client):
    courses = [COURSE, {**COURSE, "title": "CC"}, {**COURSE, "code": "CC102"}]
    responses = [client.post("/courses", json=course) for course in courses]

    get_all_courses_response = client.get("/courses")

    assert [r.status_code for r in responses] == [201, 422, 201]
    assert get_all_courses_response.json() == (
        [responses[0].json(), responses[2].json()] or
        [responses[2].json(), responses[0].json()])


@pytest.mark.parametrize("course_attribute", COURSE.keys())
def test_post_none_handling(client, course_attribute):
    course = {**COURSE, course_attribute: None}

    response = client.post("/courses", json=course)

    assert response.status_code == 422
    assert any(error["loc"] == ["body", course_attribute] for error in response.json()["detail"])
