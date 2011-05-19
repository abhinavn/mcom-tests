#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Raymond Etornam Agbeame
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****


from selenium import selenium
from unittestzero import Assert
from mozilla_base_page import MozillaBasePage


class TestCommon:
    
   
          
    def test_header_and_footer_links(self,testsetup, url="/firefox/fx/"):
        self.selenium = testsetup.selenium
        home_pg = MozillaBasePage(testsetup)
        home_pg.open(url)
        
        for x in home_pg.header_links:
            print home_pg.get_text(x)
            print home_pg.is_element_present(x)
            
        for x in home_pg.footer_support_links:
            print home_pg.get_text(x)
            print home_pg.is_element_present(x)
            
        for x in home_pg.footer_features_links:
            print home_pg.get_text(x)
            print home_pg.is_element_present(x)
            
        for  x in home_pg.footer_social_links:
            print home_pg.get_text(x)
            print home_pg.is_element_present(x)
            
        for x in home_pg.footer_mobile_links:
            print home_pg.get_text(x)
            print home_pg.is_element_present(x)
            
        for x in home_pg.footer_about_links:
            print home_pg.get_text(x)
            print home_pg.is_element_present(x)
            
        for x in home_pg.footer_addons_links:
            print home_pg.get_text(x)
            print home_pg.is_element_present(x)
            
        for x in home_pg.footer_legal_links:
            print home_pg.get_text(x)
            print home_pg.is_element_present(x)
    

    def test_all_page_header_and_footer_links(self,testsetup):
        urls = [
            "/firefox/security/",
            "/firefox/performmance/",
            "/firefox/customize/",
            "/firefox/technology/",
            "/firefox/video/",
            "/firefox/tour/",
            "/firefox/channel/",
            "/mobile/",
            "/mobile/download/",
            "/mobile/features/",
            "/mobile/customize/",
            "/mobile/sync/",
            "/mobile/getinvolved/",
            "/mobile/faq/",
            "/firefox/video/",
            "/about/",
            "/about/participate/",
            "/press/",
            "/about/careers.html",
            "/about/partnerships.html",
            "/about/legal.html",
            "/about/contact.html",
            "/firefox/all.html",
            "/firefox/all-older.html"]
            
        for x in urls:
            print x 
            self.test_header_and_footer_links(testsetup,url=x)
            
    def test_download_buttons(self,testsetup, url="/firefox/features/"):
        self.selenium = testsetup.selenium
        home_pg = MozillaBasePage(testsetup)
        home_pg.open(url)
        for x in home_pg.get_upper_download_links:
            print home_pg.get_text(x)
            print home_pg.is_element_present(x)