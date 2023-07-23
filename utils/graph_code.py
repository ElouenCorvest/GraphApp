def linegraph_code(line_number,relative_xlim_round_left, relative_xlim_round_right, abosolute_xlim_left, abosolute_xlim_right):
    code = f"""
    import matplotlib.pyplot as plt
"""
    if line_number>1:
        for i in range(1, line_number+1):
            code += f"""
    x{i} =
    y{i} = 
"""
        code += f"""
    fig, ax = plt.subplots()
"""
        for i in range(1,line_number+1):
            code += f"""
    ax.plot(x{i}, y{i})\
"""
        if relative_xlim_round_left != None:
            code += f"""

    xlim_min = min([min(i) for i in {['x' + str(j) for j in range(1, line_number+1)]}])
    xlim_min =
"""
        else:
            pass

    else:
        code += f"""
    x =
    y =

    fig, ax = plt.subplots()

    ax.plot(x, y)
"""
    xmin = 5
    n = 2
    print(xmin + (n-xmin)%n)
    return code