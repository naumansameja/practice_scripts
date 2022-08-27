class Tree_Node:
    def __init__(self, data, designation):
        self.name = data
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, data, level=1):
        if data == "both":
            print(self.name, f"({self.designation})")
        if data == "designation":
            print(self.designation)
        if data == "name":
            print(self.name)

        if self.children:
            for child in self.children:
                if self.children:
                    for i in range(level):
                        print("\t", end="")
                    print("|__", end="")
                else:
                    level -= 1
                child.print_tree(data, level + 1)


def create_tree():
    root = Tree_Node("NilPil", "CEO")
    cto = Tree_Node("Chinmay", "CTO")
    infrastructure_head = Tree_Node("Vishwa", "Infrastructure Head")
    infrastructure_head.add_child(Tree_Node("Dhawal", "Cloud Manager"))
    infrastructure_head.add_child(Tree_Node("Abhijit", "App Manager"))
    cto.add_child(infrastructure_head)
    cto.add_child(Tree_Node("Amir", "Application Head"))
    hr_head = Tree_Node("Gels", "HR Head")
    hr_head.add_child(Tree_Node("Peter", "Recruit Manager"))
    hr_head.add_child(Tree_Node("Waqas", "Policy Manager"))
    root.add_child(cto)
    root.add_child(hr_head)
    return root


def main():
    root = create_tree()
    root.print_tree("both")


main()

