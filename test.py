from rapidfuzz import fuzz, process

def test_fuzz_ratio():
    assert fuzz.ratio("hello", "hello") == 100
    assert fuzz.ratio("hello", "h3llo") < 100
    assert fuzz.ratio("hello", "world") < 50

def test_fuzz_partial_ratio():
    assert fuzz.partial_ratio("hello world", "hello") == 100
    assert fuzz.partial_ratio("goodbye world", "hello") < 100

def test_process_extract():
    choices = ["apple", "banana", "cherry", "date"]
    results = process.extract("appl", choices, scorer=fuzz.ratio, limit=2)
    assert results[0][0] == "apple"
    assert results[0][1] > 80

def run_all_tests():
    print("Running basic tests on your RapidFuzz fork...")
    test_fuzz_ratio()
    test_fuzz_partial_ratio()
    test_process_extract()
    print("✅ All tests passed!")

if __name__ == "__main__":
    run_all_tests()
