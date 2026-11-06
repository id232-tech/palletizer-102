import io
p='src/models/palletizer.py'
s=open(p).read()
body=open('autopack_body.txt').read()
route=open('autopack_route.txt').read()
q=chr(34)
if 'async def autopack' not in s:
    a='    async def move_gripper(self, pose, obstacles=None):'
    assert a in s, 'move_gripper anchor missing'
    s=s.replace(a, body.rstrip(chr(10))+chr(10)+chr(10)+a, 1)
if 'if verb == '+q+'autopack'+q+':' not in s:
    b='            return {'+q+'placed'+q+': await self.pack()}'
    assert b in s, 'pack route anchor missing'
    s=s.replace(b, b+chr(10)+chr(10)+route.rstrip(chr(10)), 1)
open(p,'w').write(s)
print('PATCHED')
