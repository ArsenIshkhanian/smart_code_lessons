# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options


# def rate_list(rate):
#     options = Options()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(options=options)
#     driver.get('https://www.rate.am/hy/armenian-dram-exchange-rates/banks')
#     driver.maximize_window()
#     dict_of_rate = {}
#     try:
#          USD = driver.find_element(By.CSS_SELECTOR, 'body > div.px-4.md\:px-0 > main > div.flex.flex-col.mx-auto.max-w-\[375px\].gap-4.reg\:flex-row-reverse.reg\:gap-6.md\:max-w-\[unset\].md\:w-736.reg\:w-\[928px\].lg\:w-1200 > div.w-full.overflow-auto.-mt-40.pt-40 > div.flex.cursor-default.grow.rounded-xl.relative.mb-1.before\:absolute.before\:inset-0.before\:pointer-events-none.before\:bottom-auto.before\:h-16.before\:border.before\:rounded-xl.before\:border-N40.before\:outline.before\:outline-\[0\.375rem\].before\:outline-white.before\:z-10.after\:z-10.after\:absolute.after\:inset-0.after\:top-\[4\.375rem\].after\:border.after\:border-N40.after\:rounded-xl.after\:pointer-events-none.after\:shadow-\[0px_4px_0px_8px_white\] > div.w-\[55\%\].grow.-mb-1.md\:w-\[60\%\].reg\:w-\[50\%\].relative.lg\:w-\[54\%\].bg-N30 > div > div.w-full.grow.bg-white > div:nth-child(1) > div:nth-child(1) > div.w-1\/2.hover\:text-O60.mx-auto.w-1\/2.false.font-bold > div > div')
#          EU = driver.find_element(By.CSS_SELECTOR, 'body > div.px-4.md\:px-0 > main > div.flex.flex-col.mx-auto.max-w-\[375px\].gap-4.reg\:flex-row-reverse.reg\:gap-6.md\:max-w-\[unset\].md\:w-736.reg\:w-\[928px\].lg\:w-1200 > div.w-full.overflow-auto.-mt-40.pt-40 > div.flex.cursor-default.grow.rounded-xl.relative.mb-1.before\:absolute.before\:inset-0.before\:pointer-events-none.before\:bottom-auto.before\:h-16.before\:border.before\:rounded-xl.before\:border-N40.before\:outline.before\:outline-\[0\.375rem\].before\:outline-white.before\:z-10.after\:z-10.after\:absolute.after\:inset-0.after\:top-\[4\.375rem\].after\:border.after\:border-N40.after\:rounded-xl.after\:pointer-events-none.after\:shadow-\[0px_4px_0px_8px_white\] > div.w-\[55\%\].grow.-mb-1.md\:w-\[60\%\].reg\:w-\[50\%\].relative.lg\:w-\[54\%\].bg-N30 > div > div.w-full.grow.bg-white > div:nth-child(1) > div:nth-child(2) > div.w-1\/2.hover\:text-O60.mx-auto.w-1\/2.false > div > div')
#          RUR = driver.find_element(By.CSS_SELECTOR, 'body > div.px-4.md\:px-0 > main > div.flex.flex-col.mx-auto.max-w-\[375px\].gap-4.reg\:flex-row-reverse.reg\:gap-6.md\:max-w-\[unset\].md\:w-736.reg\:w-\[928px\].lg\:w-1200 > div.w-full.overflow-auto.-mt-40.pt-40 > div.flex.cursor-default.grow.rounded-xl.relative.mb-1.before\:absolute.before\:inset-0.before\:pointer-events-none.before\:bottom-auto.before\:h-16.before\:border.before\:rounded-xl.before\:border-N40.before\:outline.before\:outline-\[0\.375rem\].before\:outline-white.before\:z-10.after\:z-10.after\:absolute.after\:inset-0.after\:top-\[4\.375rem\].after\:border.after\:border-N40.after\:rounded-xl.after\:pointer-events-none.after\:shadow-\[0px_4px_0px_8px_white\] > div.w-\[55\%\].grow.-mb-1.md\:w-\[60\%\].reg\:w-\[50\%\].relative.lg\:w-\[54\%\].bg-N30 > div > div.w-full.grow.bg-white > div:nth-child(1) > div:nth-child(3) > div.w-1\/2.hover\:text-O60.mx-auto.w-1\/2.false > div > div')
#          dict_of_rate['USD'] = float(USD.text.strip())
#          dict_of_rate['EU'] = float(EU.text.strip())
#          dict_of_rate['RUR'] = float(RUR.text.strip())

#     except Exception as ex:
#         print(ex.__class__.__name__)
    
#     return dict_of_rate[rate]
    



