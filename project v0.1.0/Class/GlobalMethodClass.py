from time import sleep

class GlobalMethodClass():
#public    
    def getURL(self,url):
        self.checkLoading()
        self.browser.get(url)
        self.checkLoading()
    
    def click(self,xpath):

        self.checkLoading()
        self.examinationElement(xpath)

        element = self.browser.find_element_by_xpath(xpath)
        element.click()

        self.checkLoading()

    def is_flag(self,xpath,stop = 5):
        while True:
            
            try:
                return self.browser.find_element_by_xpath(xpath)
            except:

                if (not stop):
                    return False

                sleep(0.01)
                stop-=1 

    def insData(self,data,xpath):

        self.checkLoading()

        self.examinationElement(xpath)

        inp = self.browser.find_element_by_xpath(xpath)
        inp.clear()
        inp.send_keys(data)

        self.checkLoading()

    def examinationElement(self,xpath,stop = 50):
        self.checkLoading()
        
        while True:
            try:
                data = self.browser.find_element_by_xpath(xpath) 

                self.checkLoading()

                return data

            except:

                if (not stop):
                    print('find({})'.format(xpath))
                    raise ValueError('No find '+xpath)
                sleep(0.1)
                stop-=1 

        

#private
    def checkLoading(self):

        while True:
            if (self.is_flag("//mat-spinner")):
                continue

            state = self.browser.execute_script('return document.readyState')
            
            if (not  state == "complete"):
                continue
            else:
                return        
    