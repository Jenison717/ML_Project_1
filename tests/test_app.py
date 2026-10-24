from app import app


def test_home_page():
    response = app.test_client().get("/")

    assert response.status_code == 200


def test_prediction_page_with_valid_input():
    response = app.test_client().post(
        "/predictdata",
        data={
            "gender": "male",
            "ethnicity": "group C",
            "parental_level_of_education": "high school",
            "lunch": "standard",
            "test_preparation_course": "completed",
            "reading_score": "72",
            "writing_score": "74",
        },
    )

    assert response.status_code == 200
    assert b"THE  prediction is" in response.data
