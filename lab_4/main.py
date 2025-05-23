import time
import random

A = 1860348749492490789823288813930625381760
B = 2001637506671384833171818673149062805974

def elliptic_curve(x, y, p):
    return (y ** 2) % p == (x ** 3 + (A % p) * x + (B % p)) % p

def print_curve(p):
    print(f"y^2 = x^3 + {A % p} * x + {B % p} (mod {p})")

def extended_euclidean_algorithm(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def inverse_of(n, p):
    n = n % p
    gcd, x, y = extended_euclidean_algorithm(n % p, p)
    if gcd != 1:
        raise ValueError(f"{n} has no inverse mod {p}")
    return x % p

def add_points(p1, p2, p):
    if p1 == (0, 0):
        return p2
    if p2 == (0, 0):
        return p1
    if p1[0] == p2[0] and (p1[1] + p2[1]) % p == 0:
        return (0, 0)

    if p1 == p2:
        s = ((3 * p1[0] ** 2 + A % p) * inverse_of(2 * p1[1], p)) % p
    else:
        dx = (p2[0] - p1[0]) % p
        dy = (p2[1] - p1[1]) % p
        s = (dy * inverse_of(dx, p)) % p

    x3 = (s ** 2 - p1[0] - p2[0]) % p
    y3 = (s * (p1[0] - x3) - p1[1]) % p
    return (x3, y3)

def order_point(point, p):
    result = point
    i = 1
    while result != (0, 0):
        result = add_points(result, point, p)
        i += 1
    return i

if __name__ == '__main__':
    p = 34019 

    print_curve(p)

    points = []
    start = time.time()

    for x in range(p):
        for y in range(p):
            if elliptic_curve(x, y, p):
                points.append((x, y))

    print("Total points on the curve:", len(points))

    point = random.choice(points)
    print(f"Selected point: {point}")
    print("Computing order...")

    order = order_point(point, p)
    print(f"Order of point {point}: {order}")
    print("Time elapsed: {:.3f} sec".format(time.time() - start))
