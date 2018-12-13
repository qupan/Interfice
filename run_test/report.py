#coding=utf-8
from pathlib import Path
import sys,time,unittest
addr=Path(str(Path().cwd()).split('Interfice')[0])
sys.path.append(str(addr/'Interfice'/'run_test'))
import HTMLTestRunner

#加载测试用例,返回测试用例集
def suite():
	y=str(addr/'Interfice'/'case')
	z=unittest.defaultTestLoader.discover(y,
                                              pattern="test_*.py",
                                              top_level_dir=None)
	
	return z

#运行测试用例集，生成HTML报告
def report():
	s=suite()
	x=time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
	t=str(addr/'Interfice'/"report")+"\\"+ x +"-report.html"
	y=open(t,"wb+")
	z=HTMLTestRunner.HTMLTestRunner(stream=y,
                                        title="测试结果",
                                        description="测试报告",)
	z.run(s)
	y.close()



if __name__=="__main__":
	# report()
	print(addr)


