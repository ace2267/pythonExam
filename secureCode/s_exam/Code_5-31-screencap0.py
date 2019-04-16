import win32gui
import win32api
import win32ui
import win32con

def getScreenshot():
	hwnd = win32gui.GetDesktopWindow()
	
	left, top, right, bottom = win32gui.GetWindowRect(hwnd)
	height = bottom - top
	width = right - left
	
	hDC = win32gui.GetWindowDC(hwnd)
	pDC = win32ui.CreateDCFromHandle(hDC)
	memDC = pDC.CreateCompatibleDC()
	
	screenshot = win32ui.CreateBitmap()
	screenshot.CreateCompatibleBitmap(pDC, width, height)
	memDC.SelectObject(screenshot)
	
	memDC.BitBlt((0,0), (width, height), pDC, (left, top), win32con.SRCCOPY)
	screenshot.SaveBitmapFile(memDC, 'd:/devlab/hacknsec/screenshot.bmp')
	
	memDC.DeleteDC()
	win32gui.DeleteObject(screenshot.GetHandle())
		
def main():	
	getScreenshot()	
	
if __name__ == '__main__':
	main()