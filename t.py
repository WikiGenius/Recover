from goto import with_goto


# @with_goto
# def range(start, stop):
#     i = start
#     result = []

#     label .begin
#     if i == stop:
#         goto .end

#     result.append(i)
#     i += 1
#     goto .begin

#     label .end
#     return result
@with_goto
def f():
    goto .x_y
    print("No jump")
    label .x_y
    print("jump")

f()
l = []
x = 0


def f(l, x):
    l.append(2)
    x = 5


# f(l, x)
# print(l)
# print(x)
# x = [1,2,3]
# y = reversed(x)
# print(list(y))
# print(x)

for i in range(10):
    print("{:03d}".format(i))