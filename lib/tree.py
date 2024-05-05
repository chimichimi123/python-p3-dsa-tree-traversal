class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    return self._search_tree(self.root, id)

  def _search_tree(self, node, id):
    if node is None:
      return None
    if node['id'] == id:
      return node
    for child in node['children']:
      result = self._search_tree(child, id)
      if result is not None:
        return result
    return None