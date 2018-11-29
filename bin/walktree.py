import sys
import splunk.Intersplunk

def main(results, settings):
    org = []
    keywords, options = splunk.Intersplunk.getKeywordsAndOptions()
    if len(keywords) == 2:
        parent_field = keywords[0]
        child_field = keywords[1]
    else:
        sys.exit(1)
    for result in results:
        if child_field in result and parent_field in result:
            org_dict = {"child":result[child_field],"parent":result[parent_field]}
            org.append(org_dict)
    hierarchy = walktree(org)
    results = []
    for obj in hierarchy:
        parent_dict = {}
        for key in obj:
            parent_dict = {"parent":key, "children":obj[key]}
            results.append(parent_dict)
    splunk.Intersplunk.outputResults(results)


def walktree(org):
    hierarchy = []
    parents = []
    for org_dict in org:
        if org_dict["parent"] not in parents:
            parents.append(org_dict["parent"])
    for parent in parents:
        children = get_children(parent, parents, org)
        parent_object = {parent: children}
        hierarchy.append(parent_object)
    return hierarchy


def get_children(parent, parents, org):
    children = []
    child_parents = []
    for org_dict in org:
        if org_dict["parent"] == parent:
            children.append(org_dict["child"])
    for child in children:
        if child in parents:
            child_parents.append(child)
    if len(child_parents) == 0:
        return children
    else:
        for child in child_parents:
            return children + get_children(child, parents, org)


if __name__ == "__main__":
    results, dummyresults, settings = splunk.Intersplunk.getOrganizedResults()
    main(results, settings)