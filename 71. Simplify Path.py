class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack
        # split on '/'
        # if '.' -> ignore
        # if '..' -> remove top element of stack
        dirs = path.split('/')
        dirs = [d for d in dirs if d]
        dirStack = []
        for dir in dirs:
            if dir == '.':
                continue
            elif dir == '..':
                if len(dirStack) > 0:
                    dirStack.pop()
            else:
                dirStack.append(dir)
        return '/' + '/'.join(dirStack)
