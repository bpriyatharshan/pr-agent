
# Generated by CodiumAI

import pytest
import yaml
from yaml.scanner import ScannerError

from pr_agent.algo.utils import load_yaml
from pr_agent.algo.utils import string_to_uniform_number
from pr_agent.algo.utils import is_value_no
from pr_agent.algo.utils import unique_strings
from pr_agent.algo.utils import emphasize_header


class TestLoadYaml:
    #  Tests that load_yaml loads a valid YAML string
    def test_load_valid_yaml(self):
        yaml_str = 'name: John Smith\nage: 35'
        expected_output = {'name': 'John Smith', 'age': 35}
        assert load_yaml(yaml_str) == expected_output

    def test_load_invalid_yaml1(self):
        yaml_str = \
'''\
PR Analysis:
  Main theme: Enhancing the `/describe` command prompt by adding title and description
  Type of PR: Enhancement
  Relevant tests: No
  Focused PR: Yes, the PR is focused on enhancing the `/describe` command prompt.

PR Feedback:
  General suggestions: The PR seems to be well-structured and focused on a specific enhancement. However, it would be beneficial to add tests to ensure the new feature works as expected.
  Code feedback:
    - relevant file: pr_agent/settings/pr_description_prompts.toml
      suggestion: Consider using a more descriptive variable name than 'user' for the command prompt. A more descriptive name would make the code more readable and maintainable. [medium]
      relevant line: user="""PR Info: aaa
  Security concerns: No'''
        with pytest.raises(ScannerError):
            yaml.safe_load(yaml_str)

        expected_output = {'PR Analysis': {'Main theme': 'Enhancing the `/describe` command prompt by adding title and description', 'Type of PR': 'Enhancement', 'Relevant tests': False, 'Focused PR': 'Yes, the PR is focused on enhancing the `/describe` command prompt.'}, 'PR Feedback': {'General suggestions': 'The PR seems to be well-structured and focused on a specific enhancement. However, it would be beneficial to add tests to ensure the new feature works as expected.', 'Code feedback': [{'relevant file': 'pr_agent/settings/pr_description_prompts.toml\n', 'suggestion': "Consider using a more descriptive variable name than 'user' for the command prompt. A more descriptive name would make the code more readable and maintainable. [medium]", 'relevant line': 'user="""PR Info: aaa\n'}], 'Security concerns': False}}
        assert load_yaml(yaml_str) == expected_output

    def test_load_invalid_yaml2(self):
        yaml_str = '''\
- relevant file: src/app.py:
  suggestion content: The print statement is outside inside the if __name__ ==: \
'''
        with pytest.raises(ScannerError):
            yaml.safe_load(yaml_str)

        expected_output = [{'relevant file': 'src/app.py:\n', 'suggestion content': 'The print statement is outside inside the if __name__ ==:'}]
        assert load_yaml(yaml_str) == expected_output

    def test_string_to_uniform_number(self):
        # Test basic string conversion
        result = string_to_uniform_number("test")
        assert 0 <= result <= 1
        
        # Test different strings give different numbers
        num1 = string_to_uniform_number("string1")
        num2 = string_to_uniform_number("string2")
        assert num1 != num2
        
        # Test same string gives same number
        assert string_to_uniform_number("test") == string_to_uniform_number("test")
        
        # Test empty string
        result = string_to_uniform_number("")
        assert 0 <= result <= 1


    def test_is_value_no_variations(self):
        assert is_value_no(None) is True
        assert is_value_no("") is True
        assert is_value_no("no") is True
        assert is_value_no("none") is True
        assert is_value_no("false") is True
        assert is_value_no("NO") is True
        assert is_value_no("yes") is False
        assert is_value_no("true") is False


    def test_unique_strings_with_duplicates(self):
        input_list = ["apple", "banana", "apple", "cherry", "banana"]
        result = unique_strings(input_list)
        expected = ["apple", "banana", "cherry"]
        assert result == expected
        
        # Test with empty list
        assert unique_strings([]) == []
        
        # Test with non-list input
        assert unique_strings("not a list") == "not a list"


    def test_emphasize_header_with_reference(self):
        text = "Title: This is a test"
        reference_link = "https://example.com"
        result = emphasize_header(text, only_markdown=True, reference_link=reference_link)
        expected = "[**Title:**](https://example.com)\n This is a test"
        assert result == expected





