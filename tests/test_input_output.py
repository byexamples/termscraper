import json
import os.path, sys

import pytest

import termscraper


captured_dir = os.path.join(os.path.dirname(__file__), "captured")

sys.path.append(os.path.join(os.path.dirname(__file__), "helpers"))
from asserts import consistency_asserts

@pytest.mark.parametrize("name", [
    "cat-gpl3", "find-etc", "htop", "ls", "mc", "top", "vi"
])
def test_input_output(name):
    with open(os.path.join(captured_dir, name + ".input"), "rb") as handle:
        input = handle.read()

    with open(os.path.join(captured_dir, name + ".output")) as handle:
        output = json.load(handle)

    screen = termscraper.Screen(80, 24)
    stream = termscraper.Stream(screen)
    stream.feed_binary(input)
    assert screen.display == output
    consistency_asserts(screen)

@pytest.mark.parametrize("name", [
    "cat-gpl3", "find-etc", "htop", "ls", "mc", "top", "vi"
])
def test_input_output_history(name):
    with open(os.path.join(captured_dir, name + ".input"), "rb") as handle:
        input = handle.read()

    with open(os.path.join(captured_dir, name + ".output")) as handle:
        output = json.load(handle)

    screen = termscraper.HistoryScreen(80, 24, history=72)
    stream = termscraper.Stream(screen)
    stream.feed_binary(input)
    screen.prev_page()
    screen.prev_page()
    screen.prev_page()
    screen.next_page()
    screen.next_page()
    screen.next_page()
    assert screen.display == output
    consistency_asserts(screen)

@pytest.mark.parametrize("name", [
    "cat-gpl3", "find-etc", "ls"
])
def test_input_text_output_text(name):
    with open(os.path.join(captured_dir, name + ".input"), "rb") as handle:
        input = handle.read()

    with open(os.path.join(captured_dir, name + ".output")) as handle:
        output = json.load(handle)

    # We are not emulating a real screen so there should not be whitespace
    # on the right to complete the width of the screen
    output = [line.rstrip() for line in output]

    screen = termscraper.LinearScreen()
    stream = termscraper.WSPassthroughStream(screen)
    stream.feed_binary(input)

    complete_text = screen.current_text

    # The output was designed to test a Screen of 24 lines
    # be we are not emulating a screen here so we "truncate"
    # the complete text to match 24 lines only
    truncated_display = [line.rstrip() for line in complete_text.split('\n')[-24:]]

    assert truncated_display == output
    assert not screen.were_unhandled_escape_sequences

@pytest.mark.parametrize("name", [
    "htop", "top", "vi", "mc"
])
def test_input_with_escapes_output_text(name):
    with open(os.path.join(captured_dir, name + ".input"), "rb") as handle:
        input = handle.read()

    with open(os.path.join(captured_dir, name + ".output")) as handle:
        output = json.load(handle)

    screen = termscraper.LinearScreen()
    stream = termscraper.WSPassthroughStream(screen)
    stream.feed_binary(input)

    complete_text = screen.current_text

    # The output was designed to test a Screen of 24 lines
    # be we are not emulating a screen here so we "truncate"
    # the complete text to match 24 lines only
    truncated_display = [line.rstrip() for line in complete_text.split('\n')[-24:]]

    # No real test can be made for now
    assert screen.were_unhandled_escape_sequences
    screen.stats(True)

    #print(name, screen.stats(True))
