from sentiment_analysis_models.data import pipeline


def test_process_tweet():
    pipeline.process_tweet("a")
    assert True