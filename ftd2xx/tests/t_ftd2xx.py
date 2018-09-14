#This file was originally generated by PyScripter's unitest wizard

import unittest
import ftd2xx

class TestDeviceError(unittest.TestCase):

    def setUp(self):
        self.expt = ftd2xx.DeviceError(0)

    def tearDown(self):
        pass

    def test__str__(self):
        self.assertTrue(str(self.expt) == 'OK')

class TestFTD2XX(unittest.TestCase):

    def setUp(self):
        self.device = ftd2xx.open()

    def tearDown(self):
        self.device.close()

    def testclose(self):
        pass

    def testread(self):
        self.device.setTimeouts(1000, 0)
        self.assertTrue(isinstance(self.device.read(1), str))

    def testwrite(self):
        self.assertTrue(isinstance(self.device.write('%c' % 0x0), long))

    def testioctl(self):
        pass

    def testsetBaudRate(self):
        pass

    def testsetDivisor(self):
        pass

    def testsetDataCharacteristics(self):
        pass

    def testsetFlowControl(self):
        pass

    def testresetDevice(self):
        pass

    def testsetDtr(self):
        pass

    def testclrDtr(self):
        pass

    def testsetRts(self):
        pass

    def testclrRts(self):
        pass

    def testgetModemStatus(self):
        pass

    def testsetChars(self):
        pass

    def testpurge(self):
        pass

    def testsetTimeouts(self):
        pass

    def testsetDeadmanTimeout(self):
        pass

    def testgetQueueStatus(self):
        self.assertTrue(isinstance(self.device.getQueueStatus(), long))

    def testsetEventNotification(self):
        pass

    def testgetStatus(self):
        self.assertTrue(isinstance(self.device.getStatus(), tuple))

    def testsetBreakOn(self):
        pass

    def testsetBreakOff(self):
        pass

    def testsetWaitMask(self):
        pass

    def testwaitOnMask(self):
        pass

    def testgetEventStatus(self):
        pass

    def testsetLatencyTimer(self):
        pass

    def testgetLatencyTimer(self):
        self.assertTrue(isinstance(self.device.getLatencyTimer(), int))

    def testsetBitMode(self):
        pass

    def testgetBitMode(self):
        self.assertTrue(isinstance(self.device.getBitMode(), int))

    def testsetUSBParameters(self):
        pass

    def testgetDeviceInfo(self):
        self.assertTrue(isinstance(self.device.getDeviceInfo(), dict))

    def teststopInTask(self):
        pass

    def testrestartInTask(self):
        pass

    def testsetRestPipeRetryCount(self):
        pass

    def testresetPort(self):
        pass

    def testcyclePort(self):
        pass

    def testgetDriverVersion(self):
        self.assertTrue(isinstance(self.device.getDriverVersion(), long))

    def testeeProgram(self):
        pass

    def testeeRead(self):
        self.assertTrue(isinstance(self.device.eeRead(), ftd2xx._ft.ft_program_data))

    def testeeUASize(self):
        self.assertTrue(isinstance(self.device.eeUASize(), long))

    def testeeUAWrite(self):
        pass

    def testeeUARead(self):
        self.assertTrue(isinstance(self.device.eeUARead(5), str))

class TestGlobalFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testcall_ft(self):
        pass

    def testlistDevices(self):
        self.assertTrue(isinstance(ftd2xx.listDevices(), list))

    def testgetLibraryVersion(self):
        self.assertTrue(isinstance(ftd2xx.getLibraryVersion(), long))

    def testcreateDeviceInfoList(self):
        self.assertTrue(isinstance(ftd2xx.createDeviceInfoList(), long))

    def testgetDeviceInfoDetail(self):
        self.assertTrue(isinstance(ftd2xx.getDeviceInfoDetail(), dict))

    def testopen(self):
        self.assertTrue(isinstance(ftd2xx.open(), ftd2xx.FTD2XX))

    def testopenEx(self):
        self.assertTrue(isinstance(ftd2xx.openEx(ftd2xx.listDevices()[0]), ftd2xx.FTD2XX))

    def testw32CreateFile(self):
        pass

    def testgetVIDPID(self):
        pass

    def testsetVIDPID(self):
        pass

if __name__ == '__main__':
    unittest.main()
