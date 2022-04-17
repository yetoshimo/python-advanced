from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class TestHardware(TestCase):

    def setUp(self):
        self.test_hardware = Hardware("HDD", "Power", 200, 200)

    def test_hardware_init(self):
        self.assertEqual(200, self.test_hardware.memory)
        self.assertEqual(200, self.test_hardware.capacity)
        self.assertEqual("Power", self.test_hardware.type)
        self.assertEqual("HDD", self.test_hardware.name)
        self.assertEqual([], self.test_hardware.software_components)

    def test_hardware_install_expect_exception_when_no_memory(self):
        software = ExpressSoftware("Windows", 100, 200)
        with self.assertRaises(Exception) as context:
            self.test_hardware.install(software)
        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_hardware_install_expect_exception_when_no_capacity(self):
        software = LightSoftware("Linux", 200, 100)
        with self.assertRaises(Exception) as context:
            self.test_hardware.install(software)
        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_hardware_install_success(self):
        software = LightSoftware("Linux", 10, 20)
        self.test_hardware.install(software)
        self.assertEqual(1, len(self.test_hardware.software_components))
        self.assertEqual("Linux", self.test_hardware.software_components[0].name)

    def test_hardware_install_edge_case_success(self):
        software = ExpressSoftware("Windows", 200, 100)
        self.test_hardware.install(software)
        self.assertEqual(1, len(self.test_hardware.software_components))
        self.assertEqual("Windows", self.test_hardware.software_components[0].name)

    def test_hardware_uninstall(self):
        software = LightSoftware("Linux", 10, 20)
        self.test_hardware.install(software)
        self.test_hardware.uninstall(software)
        self.assertNotIn(software, self.test_hardware.software_components)
        self.assertEqual(0, len(self.test_hardware.software_components))
        self.assertEqual([], self.test_hardware.software_components)

    def test_hardware_uninstall_non_existing_software(self):
        software = LightSoftware("Linux", 10, 20)
        software2 = ExpressSoftware("Windows", 200, 100)
        self.test_hardware.install(software)
        self.test_hardware.uninstall(software2)
        self.assertEqual(1, len(self.test_hardware.software_components))
        self.assertIn(software, self.test_hardware.software_components)


if __name__ == "__main__":
    main()
