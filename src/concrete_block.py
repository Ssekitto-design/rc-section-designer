def concrete_block(x, b, f_cd):
    alpha = 0.85
    gamma = 0.8
    a = gamma * x
    force = alpha * f_cd * b * a
    moment = force * (a / 2)
    return force, moment