class Music(object): pass
class Rock(Music): pass
class Metal(Rock): pass
class Gothic(Music): pass
class GothicRock(Rock, Gothic): pass
class GothicMetal(Metal, Gothic): pass
class The69Eyes(GothicRock, GothicMetal): pass


c = The69Eyes()
print(The69Eyes.mro())
print(The69Eyes.__mro__)

# Финальный список формируется так: сначала добавляется данный класс,
# потом рассматривается первый класс из линеаризации первого родителя,
# если он не встречается в других списках,
# то добавляется в финальный и так далее.
# Если участвует, то переходим к рассмотрению следующего родителя.

# (<class '__main__.The69Eyes'>, <class '__main__.GothicRock'>,
# <class '__main__.GothicMetal'>, <class '__main__.Metal'>,
# <class '__main__.Rock'>, <class '__main__.Gothic'>,
# <class '__main__.Music'>, <class 'object'>)

#        Music
#       /      \
#    Rock      Gothic ------
#    /     \        /       \
# Metal    Gothic Rock       \
#   |             |           \
#    \------------------ Gothic Metal
#                 |          /
#                 The 69 Eyes
