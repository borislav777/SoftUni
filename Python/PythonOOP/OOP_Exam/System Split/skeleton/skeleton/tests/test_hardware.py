import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("Intel", "Power", 100, 200)

    def test_init(self):
        self.assertEqual("Intel", self.hardware.name)
        self.assertEqual("Power", self.hardware.type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(200, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_install_valid(self):
        software = ExpressSoftware("Nero", 20, 50)
        self.hardware.install(software)
        self.assertEqual([software], self.hardware.software_components)

    def test_install_dont_have_memory_and_capacity(self):
        software = ExpressSoftware("Nero", 150, 250)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)

        self.assertEqual("Software cannot be installed", str(ex.exception))
        self.assertEqual([], self.hardware.software_components)

    def test_uninstall(self):
        software = ExpressSoftware("Nero", 20, 50)
        self.hardware.software_components = [software]
        self.assertEqual([software], self.hardware.software_components)
        self.hardware.uninstall(software)
        self.assertEqual([], self.hardware.software_components)


if __name__ == "__main__":
    unittest.main()
