class ValidationError(ValueError):
    pass

class Validator:
    def __init__(self):
        self.pairs = {')': '(', '}': '{', '>': '<'}
        self.openers = set(self.pairs.values())

    def _is_balanced(self, input_text: str) -> list[int]:
        stack = []
        errors = []
        for i, char in enumerate(input_text):
            if char in self.openers:
                stack.append((char, i))
            elif char in self.pairs:
                if stack and stack[-1][0] == self.pairs[char]:
                    stack.pop()
                else:
                    errors.append(i)
        for char, i in stack:
            errors.append(i)
        return sorted(errors)

    def validate(self, input_text: str) -> bool:
        errors = self._is_balanced(input_text)
        if errors:
            visual = [' '] * len(input_text)
            for idx in errors:
                visual[idx] = '^'
            print(input_text)
            print("".join(visual))
            positions = ", ".join(map(str, errors))
            raise ValidationError(f"Дужки незбалансовані на позиціях {positions}")
        return True