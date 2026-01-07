from chapter5.LinkStack import LinkStack, Stack


class TestLinkStack:
    def test_link_stack(self):
        stack = LinkStack()
        stack.push(10)
        stack.push(20)
        assert len(stack) == 2
        assert stack.peek() == 20
        assert stack.pop() == 20
        assert len(stack) == 1
        assert stack.pop() == 10
        assert stack.isEmpty()

    def test_stack(self):
        stack = Stack()
        stack.push(30)
        stack.push(40)
        assert len(stack) == 2
        assert stack.peek() == 40
        assert stack.pop() == 40
        assert len(stack) == 1
        assert stack.pop() == 30
        assert stack.isEmpty()
