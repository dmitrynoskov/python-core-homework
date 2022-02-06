def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    return \
        {
            "categories":
                [
                    {
                        "id": f"category-{category_id}",
                        "text": mapping["categories"][category_id]["name"],
                        "items":
                            [
                                {
                                    "id": role_id,
                                    "text": mapping["roles"][role_id]["name"]
                                } for role_id in mapping["categories"][category_id]["roleIds"]
                            ]
                    } for category_id in mapping["categoryIdsSorted"]
                ]
        }
