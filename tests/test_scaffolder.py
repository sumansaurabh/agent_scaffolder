import unittest
import os
import shutil
from src.scaffolder import AgentScaffolder

class TestProjectCreator(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_project"
        self.structure_file = "test_structure.txt"
        with open(self.structure_file, 'w') as file:
            file.write("project_creator/\n")
            file.write("├── project_creator/\n")
            file.write("│   ├── __init__.py\n")
            file.write("│   ├── creator.py\n")
            file.write("├── tests/\n")
            file.write("│   ├── __init__.py\n")
            file.write("│   ├── test_creator.py\n")
            file.write("├── setup.py\n")
            file.write("├── README.md\n")
            file.write("├── LICENSE\n")
            file.write("├── .gitignore\n")
            file.write("├── requirements.txt\n")
        self.creator = AgentScaffolder(self.structure_file, self.test_dir)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        if os.path.exists(self.structure_file):
            os.remove(self.structure_file)

    def test_create_project_structure(self):
        self.creator.create_project_structure()
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "project_creator/project_creator/__init__.py")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "project_creator/project_creator/creator.py")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "project_creator/tests/__init__.py")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "project_creator/tests/test_creator.py")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "project_creator/setup.py")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "project_creator/README.md")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "project_creator/LICENSE")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "project_creator/.gitignore")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "project_creator/requirements.txt")))

if __name__ == "__main__":
    unittest.main()
