""" Namespace emulation
Программе на вход подаются следующие запросы:
    create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
    add <namespace> <var> – добавить в пространство <namespace> переменную <var>
    get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
    пространства <namespace>, или None, если такого пространства не существует """


def namespace_emul(operator, ns, var):
    if operator == 'get':
        if variables.get(ns) is not None and var in variables[ns]:
            print(ns)
            return
        elif ns == 'global':
            print('None')
            return
        else:  # if var not in variables[ns]
            for namesp, lst in namespaces.items():
                if ns in lst:
                    namespace_emul(operator, namesp, var)
                    return
            print('None')
            return
    elif operator == 'add':  # add a variable
        if variables.get(ns) is None:
            variables[ns] = [var]
        else:
            variables[ns] += [var]
    elif operator == 'create':  # create a namespace
        namespaces[var].append(ns)
        namespaces[ns] = []


if __name__ == '__main__':
    namespaces = {'global': []}
    variables = {}
    for i in range(int(input())):
        namespace_emul(*input().split())
