from app.streamlit_app import confidence_label


def test_confidence_label_high():
    assert confidence_label(0.30) == "High"


def test_confidence_label_medium():
    assert confidence_label(0.10) == "Medium"


def test_confidence_label_low():
    assert confidence_label(0.01) == "Low"
