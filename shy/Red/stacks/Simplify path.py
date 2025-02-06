'''
given an absolute path for a Unix-style file system which always begins with a slash '/'.
Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.

Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name.
For example, '...' and '....' are valid directory or file names.

The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
'''

'''
Example 2:
Input: path = "/home//foo/"
Output: "/home/foo"

Example 3:
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"

Example 5:
Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
'''

'''
Constraints:
1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
'''

# 给定的路径只有几种形式，分情况处理。 返回上级目录或保持当前目录
# 使用stack记录路径
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for portion in path.split('/'):
            if portion == '..':
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                continue
            else:
                stack.append(portion)

        # 按照格式拼接答案
        final_path = "/" + "/".join(stack)
        return final_path