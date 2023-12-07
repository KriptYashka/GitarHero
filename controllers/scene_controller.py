class SceneController:
    scene_changed = True
    scene_name = "Menu"

    @staticmethod
    def set_scene(scene_name: str):
        SceneController.scene_changed = True
        SceneController.scene_name = scene_name

    @staticmethod
    def set_menu_scene():
        SceneController.set_scene("Menu")
