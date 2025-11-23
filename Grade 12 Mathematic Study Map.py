from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.config import Config

#Window.keyboard_anim_args = {"d":.2, "t":"in_out_expo"} # Transition
#Window.softinput_mode = "below_target" # It

#Window.clearcolor = (0, 0.6, 0.1, 1.0)    
#Window.size = (400, 600)


home_of_kv="""
#:import Window kivy.core.window.Window
#mport IconLeftWidget kivymd.uix.list.IconLeftWidget
#:import sm kivy.uix.screenmanager
#:set color_shadow [0, 0, 0, .2980392156862745]
#:import sys sys
ScreenManager:
	transition:sm.NoTransition()
    Years_Screen:
    Six_Screen:
    Six_March_February_Screen:
    Six_March_February_Paper_One_SG_Screen:
    Six_March_February_Paper_Two_SG_Screen:
    Six_March_February_Paper_One_HG_Screen:
    Six_March_February_Paper_Two_HG_Screen:
    Six_November_Screen:
    Six_November_Paper_One_HG_Screen: 
    Six_November_Paper_Two_HG_Screen:    
    Text_Book_Screen:
    Text_Book_Via_Africa_Screen: 
    

<Years_Screen>:
    name:"years"
    GridLayout:
        id: grid_layout
        cols: 1
        rows: 5
        padding: dp(5)
        spacing: dp(0)

        Label:
            text: "GRADE 12 MATHEMATICS STUDY MAP"
            font_size: 25
            size_hint_y: None
            height: dp(60)
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1  # Blue color
                Rectangle:
                    pos: self.pos
                    size: self.size 

            
        GridLayout:
            cols:1
            rows:1
            size_hint_y:None
            height:dp(48)
            TextInput:
                id:search_entry
                hint_text:"Search here..."
                size_hint_y:None
                height:dp(48)
                on_text:root.searching()            
            

        ScrollView:
            do_scroll_y:True
            bar_width:20
            GridLayout:
                cols:1
                size_hint_y:None
                height:self.minimum_height
                spacing:dp(2)
                
                Button:
                    text:"Text Books"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'textbook'                 
                
                Button:
                    text:"Study Guides"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'years'
                                               
                Button:
                    text:"NBT"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'years'                                      

                Button:
                    text:"IEB"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'six'
                Button:
                    text:"2006"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'six'                         
                
                Button:
                    text:"2007"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'                
                
                Button:
                    text:"2008"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'                
                
                Button:
                    text:"2009"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'

                Button:
                    text:"2010"
                    size_hint_y:None#
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'

                Button:
                    text:"2011"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'

                Button:
                    text:"2012"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'

                Button:
                    text:"2013"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'

                Button:
                    text:"2014"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'
                        
                Button:
                    text:"2015"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'
                        
                Button:
                    text:"2016"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'

                Button:
                    text:"2017"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'

                Button:
                    text:"2018"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'                                                                                                                                        
 
                Button:
                    text:"2019"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'                
                
                Button:
                    text:"2020"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'                
                
                Button:
                    text:"2021"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'

                Button:
                    text:"2022"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'

                Button:
                    text:"2023"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'

                Button:
                    text:"2024"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1                    
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'Years'                       
<Text_Book_Screen>:
    name:"textbook"
    GridLayout:
        cols: 1
        rows: 3
        padding: dp(1)
        spacing: dp(0)
        BoxLayout:
            orientation:"horizontal"
            #cols: 2
            #rows: 1
            padding: dp(1)
            spacing: dp(0)
            size_hint_y:None
            height:dp(48)
            Button: 
                size_hint_y: None
                height:dp(48)
                size_hint_x:None
                width:dp(50)
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = "years"
                background_color:0,0,0,0
                canvas.before:
                    Color:
                        rgba: 1,1,1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size   
                        source:"icon/back.png"   
                
            Label:
                text: "Text Books"
                font_size: 55
                size_hint_y: None
                height:dp(48)
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size         
        
        ScrollView:
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(0)
                
                Button:
                    text:"Via Afrika"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'textbook via africa'

                Button:
                    text:"Platinum"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'textbook'

<Text_Book_Via_Africa_Screen>:
    name:"textbook via africa"
    GridLayout:
        cols: 1
        rows: 3
        padding: dp(1)
        spacing: dp(0)
        BoxLayout:
            orientation:"horizontal"
            #cols: 2
            #rows: 1
            padding: dp(1)
            spacing: dp(0)
            size_hint_y:None
            height:dp(48)
            Button: 
                size_hint_y: None
                height:dp(48)
                size_hint_x:None
                width:dp(50)
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = "textbook"
                background_color:0,0,0,0
                canvas.before:
                    Color:
                        rgba: 1,1,1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size   
                        source:"icon/back.png"   
                
            Label:
                text: "Via Afrika"
                font_size: 55
                size_hint_y: None
                height:dp(48)
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size         
        
        ScrollView:
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(0)
                
                ToggleButton:
                    text:"Via Afrika"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_Text_Book_Via_Africa()

                Image:
                    id: img
                    source:"Text Books\Gr12-Mathematics-Study-Guide_LR\Gr12-Mathematics-Study-Guide_LR_1.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: img2
                    source:"Text Books\Gr12-Mathematics-Study-Guide_LR\Gr12-Mathematics-Study-Guide_LR_1.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: img3
                    source:"Text Books\Gr12-Mathematics-Study-Guide_LR\Gr12-Mathematics-Study-Guide_LR_3.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True
<Six_Screen>:
    name:"six"
    GridLayout:
        cols: 1
        rows: 3
        padding: dp(1)
        spacing: dp(0)
        BoxLayout:
            orientation:"horizontal"
            #cols: 2
            #rows: 1
            padding: dp(1)
            spacing: dp(0)
            size_hint_y:None
            height:dp(48)
            Button: 
                size_hint_y: None
                height:dp(48)
                size_hint_x:None
                width:dp(50)
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = "years"
                background_color:0,0,0,0
                canvas.before:
                    Color:
                        rgba: 1,1,1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size   
                        source:"icon/back.png"   
                
            Label:
                text: "2006"
                font_size: 55
                size_hint_y: None
                height:dp(48)
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size         
        
        ScrollView:
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(0)
                
                Button:
                    text:"March/February"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'six_march_february'

                Button:
                    text:"November"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'six_november'
                                                                                                                                                                                                
<Six_March_February_Screen>:
    name:"six_march_february"
    GridLayout:
        cols: 1
        rows: 3
        padding: dp(1)
        spacing: dp(0)
        BoxLayout:
            orientation:"horizontal"
            #cols: 2
            #rows: 1
            padding: dp(1)
            spacing: dp(0)
            size_hint_y:None
            height:dp(48)
            Button: 
                size_hint_y: None
                height:dp(48)
                size_hint_x:None
                width:dp(50)
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = "six"
                background_color:0,0,0,0
                canvas.before:
                    Color:
                        rgba: 1,1,1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size   
                        source:"icon/back.png"   
                
            Label:
                text: "March/February"
                font_size: 50
                size_hint_y: None
                height:dp(48)
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size         
        
        ScrollView:
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(0)
                
                Button:
                    text:"Paper 1(SG)"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'six_march_february_paper_one_sg'

                Button:
                    text:"Paper 2(SG)"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'six_march_february_paper_two_sg' 

                Button:
                    text:"Paper 1(HG)"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'six_march_february_paper_one_hg'

                Button:
                    text:"Paper 2(HG)"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'six_march_february_paper_two_hg'                                

<Six_March_February_Paper_One_SG_Screen>:
    name:"six_march_february_paper_one_sg"
    GridLayout:
        cols: 1
        rows: 3
        padding: dp(1)
        spacing: dp(0)
        BoxLayout:
            orientation:"horizontal"
            #cols: 2
            #rows: 1
            padding: dp(1)
            spacing: dp(0)
            size_hint_y:None
            height:dp(48)
            Button: 
                size_hint_y: None
                height:dp(48)
                size_hint_x:None
                width:dp(50)
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = "six_march_february"
                background_color:0,0,0,0
                canvas.before:
                    Color:
                        rgba: 1,1,1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size   
                        source:"icon/back.png"   
                
            Label:
                text: "Paper 1(SG)"
                font_size: 43
                size_hint_y: None
                height:dp(48)
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size         
        
        ScrollView:
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(0)
                

                ToggleButton:
                    text:"Question 1"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_one()               
                

                Image:
                    id: img
                    source:"D:\Grade 12 Mathematic\six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper\one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo()

                Image:
                    id: memo_img
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An\one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_img2
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An\ones.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 2"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_two()

                Image:
                    id: question_two_img
                    source:"six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper/two.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_two()

                Image:
                    id: memo_two_img
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An/two.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True
                    
                Image:
                    id: memo_two_img2
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An/twos.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                  

                ToggleButton:
                    text:"Question 3"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_three()

                Image:
                    id: question_three_img
                    source:"six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper/three.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_three()

                Image:
                    id: memo_three_img
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An/three.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                     

                ToggleButton:
                    text:"Question 4"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_four()

                Image:
                    id: question_four_img
                    source:"six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper/four.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    
                    
                Image:
                    id: question_four_img2
                    source:"six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper/fours.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True
                                    
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_four()

                Image:
                    id: memo_four_img
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An/four.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 5"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_five()

                Image:
                    id: question_five_img
                    source:"six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper/five.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_five()

                Image:
                    id: memo_five_img
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An/five.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_fives_img2
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An/fives.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    

                    
                ToggleButton:
                    text:"Question 6"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_six()

                Image:
                    id: question_six_img
                    source:"six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper\six.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_six()

                Image:
                    id: memo_six_img
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An\six.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_sixs_img2
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An\sixs.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                ToggleButton:
                    text:"Question 7"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_seven()

                Image:
                    id: question_seven_img
                    source:"six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper\seven.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_seven()

                Image:
                    id: memo_seven_img
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An\seven.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 8"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_eight()

                Image:
                    id: question_eight_img
                    source:"six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper/eight.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    
                    
                Image:
                    id: question_eights_img2
                    source:"six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper/eights.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True
                                    
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_eight()

                Image:
                    id: memo_eight_img
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An/eight.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                Image:
                    id: memo_eights_img2
                    source:"six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An\eights.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                ToggleButton:
                    text:"Formula Sheet"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_formula_sheet()

                Image:
                    id: formula_sheet_img
                    source:"six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper/formula sheet.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    
                                        
                    
<Six_March_February_Paper_Two_SG_Screen>:
    name:"six_march_february_paper_two_sg"
    GridLayout:
        cols: 1
        rows: 3
        padding: dp(1)
        spacing: dp(0)
        BoxLayout:
            orientation:"horizontal"
            #cols: 2
            #rows: 1
            padding: dp(1)
            spacing: dp(0)
            size_hint_y:None
            height:dp(48)
            Button: 
                size_hint_y: None
                height:dp(48)
                size_hint_x:None
                width:dp(50)
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = "six_march_february"
                background_color:0,0,0,0
                canvas.before:
                    Color:
                        rgba: 1,1,1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size   
                        source:"icon/back.png"   
                
            Label:
                text: "Paper 2(SG)"
                font_size: 43
                size_hint_y: None
                height:dp(48)
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size         
        
        ScrollView:
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(0)                    

                ToggleButton:
                    text:"Question 1"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_one()               
                
                Image:
                    id: img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper\one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                                
              
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo()

                Image:
                    id: memo_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_img2
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\ones.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                Image:
                    id: memo_img3
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\oness.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_img4
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\onesss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                       

                Image:
                    id: memo_img5
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\onessss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 2"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_two()

                Image:
                    id: question_two_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper/two.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                     

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_two()

                Image:
                    id: memo_two_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers/two.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                ToggleButton:
                    text:"Question 3"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_three()

                Image:
                    id: question_three_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper/three.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_three()

                Image:
                    id: memo_three_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers/three.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    

                ToggleButton:
                    text:"Question 4"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_four()

                Image:
                    id: question_four_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper/four.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True   

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_four()

                Image:
                    id: memo_four_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers/four.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                ToggleButton:
                    text:"Question 5"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_five()

                Image:
                    id: question_five_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper/five.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_five()

                Image:
                    id: memo_five_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers/five.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 6"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_six()

                Image:
                    id: question_six_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper\six.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_six()

                Image:
                    id: memo_six_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\six.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 7"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_seven()

                Image:
                    id: question_seven_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper\seven.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: question_seven_img2
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper\sevens.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                
                
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_seven()

                Image:
                    id: memo_seven_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\seven.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_sevens_img2
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\sevens.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                                        

                ToggleButton:
                    text:"Question 8"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_eight()

                Image:
                    id: question_eight_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper\eight.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    
                    
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_eight()

                Image:
                    id: memo_eight_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\eight.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 


                ToggleButton:
                    text:"Question 9"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_nine()

                Image:
                    id: question_nine_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper/nine.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    
                    
                Image:
                    id: question_nine_img2
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper/nines.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True
                                    
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_nine()

                Image:
                    id: memo_nine_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers/nine.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                Image:
                    id: memo_nine_img2
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers/nines.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                ToggleButton:
                    text:"Formula Sheet"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_formula_sheet()

                Image:
                    id: formula_sheet_img
                    source:"six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper/formula 2.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

<Six_March_February_Paper_One_HG_Screen>:
    name:"six_march_february_paper_one_hg"
    GridLayout:
        cols: 1
        rows: 3
        padding: dp(1)
        spacing: dp(0)
        BoxLayout:
            orientation:"horizontal"
            #cols: 2
            #rows: 1
            padding: dp(1)
            spacing: dp(0)
            size_hint_y:None
            height:dp(48)
            Button: 
                size_hint_y: None
                height:dp(48)
                size_hint_x:None
                width:dp(50)
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = "six_march_february"
                background_color:0,0,0,0
                canvas.before:
                    Color:
                        rgba: 1,1,1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size   
                        source:"icon/back.png"   
                
            Label:
                text: "Paper 1(HG)"
                font_size: 43
                size_hint_y: None
                height:dp(48)
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size         
        
        ScrollView:
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(0)
                

                ToggleButton:
                    text:"Question 1"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_one()               

                Image:
                    id: img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)\one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo()

                Image:
                    id: memo_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_img2
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/ones.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                Image:
                    id: memo_img3
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/oness.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 

                ToggleButton:
                    text:"Question 2"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_two()

                Image:
                    id: question_two_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)/two.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                     

                Image:
                    id: question_two_img2
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)/twos.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_two()

                Image:
                    id: memo_two_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/two.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 

                Image:
                    id: memo_two_img2
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/twos.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                     

                ToggleButton:
                    text:"Question 3"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_three()

                Image:
                    id: question_three_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)/three.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_three()

                Image:
                    id: memo_three_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/three.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    

                ToggleButton:
                    text:"Question 4"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_four()

                Image:
                    id: question_four_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)/four.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True   

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_four()

                Image:
                    id: memo_four_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/four.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                      

                Image:
                    id: memo_four_img2
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/fours.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 5"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_five()

                Image:
                    id: question_five_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)/five.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: question_fives_img2
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)/fives.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_five()

                Image:
                    id: memo_five_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/five.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_fives_img2
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/fives.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                ToggleButton:
                    text:"Question 6"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_six()

                Image:
                    id: question_six_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)\six.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_six()

                Image:
                    id: memo_six_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers\six.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_six_img2
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers\sixs.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 7"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_seven()

                Image:
                    id: question_seven_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)\seven.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True
                               
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_seven()

                Image:
                    id: memo_seven_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers\seven.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_sevens_img2
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers\sevens.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 8"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_eight()

                Image:
                    id: question_eight_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)\eight.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    
                                                        
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_eight()

                Image:
                    id: memo_eight_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers\eight.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                ToggleButton:
                    text:"Formula Sheet"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_formula_sheet()

                Image:
                    id: formula_sheet_img
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)/formula sheet.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    
                      
<Six_March_February_Paper_Two_HG_Screen>:
    name:"six_march_february_paper_two_hg"
    GridLayout:
        cols: 1
        rows: 3
        padding: dp(1)
        spacing: dp(0)
        BoxLayout:
            orientation:"horizontal"
            #cols: 2
            #rows: 1
            padding: dp(1)
            spacing: dp(0)
            size_hint_y:None
            height:dp(48)
            Button: 
                size_hint_y: None
                height:dp(48)
                size_hint_x:None
                width:dp(50)
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = "six_march_february"
                background_color:0,0,0,0
                canvas.before:
                    Color:
                        rgba: 1,1,1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size   
                        source:"icon/back.png"   
                
            Label:
                text: "Paper 2(HG)"
                font_size: 43
                size_hint_y: None
                height:dp(48)
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size         
        
        ScrollView:
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(0)                    

                ToggleButton:
                    text:"Question 1"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_one()               
                
                Image:
                    id: img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)\one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True   

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo()

                Image:
                    id: memo_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_img2
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\ones.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                Image:
                    id: memo_img3
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\oness.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                     

                ToggleButton:
                    text:"Question 2"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_two()

                Image:
                    id: question_two_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)/two.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                     
                    
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_two()

                Image:
                    id: memo_two_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/two.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 

                Image:
                    id: memo_two_img2
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/twos.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True
                                        
                Image:
                    id: memo_two_img3
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/twoss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 3"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_three()

                Image:
                    id: question_three_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)/three.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_three()

                Image:
                    id: memo_three_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/three.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    

                ToggleButton:
                    text:"Question 4"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_four()

                Image:
                    id: question_four_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)/four.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True   

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_four()

                Image:
                    id: memo_four_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/four.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_four_img2
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/fours.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True
                    
                ToggleButton:
                    text:"Question 5"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_five()

                Image:
                    id: question_five_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)/five.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_five()

                Image:
                    id: memo_five_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/five.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 6"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_six()

                Image:
                    id: question_six_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)\six.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: question_six_img2
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)\sixs.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True             
                                        
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_six()

                Image:
                    id: memo_six_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\six.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_six_img2
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\sixss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_six_img3
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers\sixs.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 7"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_seven()

                Image:
                    id: question_seven_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)\seven.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_seven()
                                        
                Image:
                    id: memo_seven_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\seven.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                ToggleButton:
                    text:"Question 8"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_eight()

                Image:
                    id: question_eight_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)\eight.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: question_eight_img2
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)\eights.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True             
                                        
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_eight()

                Image:
                    id: memo_eight_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\eight.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_eight_img2
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\eights.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Question 9"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_nine()

                Image:
                    id: question_nine_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)/nine.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_nine()

                Image:
                    id: memo_nine_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/nine.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_nine_img2
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/nines.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                ToggleButton:
                    text:"Question 10"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_ten()

                Image:
                    id: question_ten_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)/ten.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: question_ten_img2
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)/tens.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True             
                                        
                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_ten()

                Image:
                    id: memo_ten_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/ten.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_ten_img2
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/tens.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                Image:
                    id: memo_ten_img3
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/tenss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True  
                    
                ToggleButton:
                    text:"Formula Sheet"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_formula_sheet()

                Image:
                    id: formula_sheet_img
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)/formular sheet.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

<Six_November_Screen>:
    name:"six_november"
    GridLayout:
        cols: 1
        rows: 3
        padding: dp(1)
        spacing: dp(0)
        BoxLayout:
            orientation:"horizontal"
            #cols: 2
            #rows: 1
            padding: dp(1)
            spacing: dp(0)
            size_hint_y:None
            height:dp(48)
            Button: 
                size_hint_y: None
                height:dp(48)
                size_hint_x:None
                width:dp(50)
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = "six"
                background_color:0,0,0,0
                canvas.before:
                    Color:
                        rgba: 1,1,1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size   
                        source:"icon/back.png"   
                
            Label:
                text: "November"
                font_size: 50
                size_hint_y: None
                height:dp(48)
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size         
        
        ScrollView:
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(0)
                
                Button:
                    text:"Paper 1"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'six_november_paper_one_hg'

                Button:
                    text:"Paper 2"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
                        root.manager.current = 'six_november_paper_two_hg'                    

<Six_November_Paper_One_HG_Screen>:
    name:"six_november_paper_one_hg"
    GridLayout:
        cols: 1
        rows: 3
        padding: dp(1)
        spacing: dp(0)
        BoxLayout:
            orientation:"horizontal"
            #cols: 2
            #rows: 1
            padding: dp(1)
            spacing: dp(0)
            size_hint_y:None
            height:dp(48)
            Button: 
                size_hint_y: None
                height:dp(48)
                size_hint_x:None
                width:dp(50)
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = "six_november"
                background_color:0,0,0,0
                canvas.before:
                    Color:
                        rgba: 1,1,1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size   
                        source:"icon/back.png"   
                
            Label:
                text: "Paper 1(HG)"
                font_size: 43
                size_hint_y: None
                height:dp(48)
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size         
        
        ScrollView:
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(0)
                

                ToggleButton:
                    text:"Question 1"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_one()               

                Image:
                    id: img
                    source:"six/November/paper 1 HG/November 2006 Question Paper/one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo()

                Image:
                    id: memo_img
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_img2
                    source:"six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/ones.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                Image:
                    id: memo_img3
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/oness.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 
                        
                Image:
                    id: memo_img4
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/onesss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                Image:
                    id: memo_img5
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/onessss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 
 
                ToggleButton:
                    text:"Question 2"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_two()

                Image:
                    id: question_two_img
                    source:"six/November/paper 1 HG/November 2006 Question Paper/two.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True   

                Image:
                    id: question_two_img2
                    source:"six/November/paper 1 HG/November 2006 Question Paper/twos.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True   

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_two()

                Image:
                    id: memo_two_img
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/two.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 

                Image:
                    id: memo_two_img2
                    source:"six\paper 2 HG\Grade 12 SC Mathematics "
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True
                                        
                Image:
                    id: memo_two_img3
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/twoss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True
 
                Image:
                    id: memo_two_img4
                    source:"six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/twoss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                                    

                ToggleButton:
                    text:"Question 3"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_three()

                Image:
                    id: question_three_img
                    source:"six/November/paper 1 HG/November 2006 Question Paper/three.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_three()

                Image:
                    id: memo_three_img
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/three.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    

                Image:
                    id: memo_three_img2
                    source:"six\paper 2 HG/Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/three.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    

                ToggleButton:
                    text:"Question 4"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_four()

                Image:
                    id: question_four_img
                    source:"six/November/paper 1 HG/November 2006 Question Paper/four.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_four()

                Image:
                    id: memo_four_img
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/four.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    

                Image:
                    id: memo_four_img2
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/fours.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 

                ToggleButton:
                    text:"Question 5"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_five()

                Image:
                    id: question_five_img
                    source:"six/November/paper 1 HG/November 2006 Question Paper/five.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_five()

                Image:
                    id: memo_five_img
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/five.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    

                Image:
                    id: memo_five_img2
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/fives.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 

                Image:
                    id: memo_five_img3
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/fivess.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 

                Image:
                    id: memo_five_img4
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/fivesss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 

                ToggleButton:
                    text:"Question 6"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_six()

                Image:
                    id: question_six_img
                    source:"six/November/paper 1 HG/November 2006 Question Paper/six.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_six()

                Image:
                    id: memo_six_img
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/six.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    

                Image:
                    id: memo_six_img2
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/sixs.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 

                ToggleButton:
                    text:"Question 7"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_seven()

                Image:
                    id: question_seven_img
                    source:"six/November/paper 1 HG/November 2006 Question Paper/seven.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_seven()

                Image:
                    id: memo_seven_img
                    source:"six/November/paper 1 HG/November 2006 Possible Answers/seven.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    

                ToggleButton:
                    text:"Question 8"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_eight()

                Image:
                    id: question_eight_img
                    source:"six/November/paper 1 HG/November 2006 Question Paper/eight.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Formula Sheet"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_formula_sheet()

                Image:
                    id: formula_sheet_img
                    source:"six/November/paper 1 HG/November 2006 Question Paper/formular sheet.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

<Six_November_Paper_Two_HG_Screen>:
    name:"six_november_paper_two_hg"
    GridLayout:
        cols: 1
        rows: 3
        padding: dp(1)
        spacing: dp(0)
        BoxLayout:
            orientation:"horizontal"
            #cols: 2
            #rows: 1
            padding: dp(1)
            spacing: dp(0)
            size_hint_y:None
            height:dp(48)
            Button: 
                size_hint_y: None
                height:dp(48)
                size_hint_x:None
                width:dp(50)
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 0.5
                    root.manager.current = "six_november"
                background_color:0,0,0,0
                canvas.before:
                    Color:
                        rgba: 1,1,1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size   
                        source:"icon/back.png"   
                
            Label:
                text: "Paper 2(HG)"
                font_size: 43
                size_hint_y: None
                height:dp(48)
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 1  # Blue color
                    Rectangle:
                        pos: self.pos
                        size: self.size         
        
        ScrollView:
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(0)
                

                ToggleButton:
                    text:"Question 1"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_one()               

                Image:
                    id: img
                    source:"six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Question Paper/one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo()

                Image:
                    id: memo_img
                    source:"six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_img2
                    source:"six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/ones.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True                    

                Image:
                    id: memo_img3
                    source:"six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/oness.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 
                        
                Image:
                    id: memo_img4
                    source:"six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/one.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True    

                ToggleButton:
                    text:"Question 2"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_question_two()

                Image:
                    id: question_two_img
                    source:"six/November/paper 1 HG/November 2006 Question Paper/two.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True   

                ToggleButton:
                    text:"Memo"
                    size_hint_y:None
                    height:dp(48)
                    background_color : 0, 0, 1, 1
                    on_press: root.show_memo_two()

                Image:
                    id: memo_two_img
                    source:"six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/two.PNG"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_two_img2
                    source:"six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/twos.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_two_img3
                    source:"six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/twoss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True 

                Image:
                    id: memo_two_img4
                    source:"six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/twosss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

                Image:
                    id: memo_two_img5
                    source:"six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/twossss.png"
                    size_hint_y:None
                    height:dp(0)
                    keep_ratio:False
                    allow_stretch:True

            


        
"""

class Years_Screen(Screen):
    
    def searching(self):
        manager = ScreenManager()

        if "NBT" in self.ids.search_entry.text:
            App.get_running_app().manager.current = "NBT"
                   
        if "2006" in self.ids.search_entry.text:
            App.get_running_app().manager.current = "six"       
        
        if "ACCOUNTING" in self.ids.search_entry.text:
            App.get_running_app().manager.current = "accounting"                
      
        
        if "math" in self.ids.search_entry.text:#or "mathematics" in self.ids.search_entry.text or "math" in self.ids.search_entry.text:
            App.get_running_app().manager.current = "mathematics"
        elif "physical" in self.ids.search_entry.text:
            App.get_running_app().manager.current = "physical_science_screen"
        else:
            pass

    def on_search_button_press(self):
        # Call the searching method when the "Search" button is pressed
        self.searching()

class Text_Book_Screen(Screen):
    pass

class Text_Book_Via_Africa_Screen(Screen):
    
    def show_Text_Book_Via_Africa(self):
        if self.ids.img.height == dp(0):
            self.ids.img.height = dp(535)
            self.ids.img.width = dp(410)

            self.ids.img2.source = "Text Books\Gr12-Mathematics-Study-Guide_LR\Gr12-Mathematics-Study-Guide_LR_2.png"
            self.ids.img2.height = dp(535)
            self.ids.img2.width = dp(400)

            self.ids.img3.source = "Text Books\Gr12-Mathematics-Study-Guide_LR\Gr12-Mathematics-Study-Guide_LR_3.png"
            self.ids.img3.height = dp(535)
            self.ids.img3.width = dp(400)

            self.ids.img3.source = "Text Books\Gr12-Mathematics-Study-Guide_LR\Gr12-Mathematics-Study-Guide_LR_3.png"
            self.ids.img3.height = dp(535)
            self.ids.img3.width = dp(400)
            
class Six_Screen(Screen):
    pass

class Six_March_February_Screen(Screen):
    pass

class Six_March_February_Paper_One_SG_Screen(Screen):
    
    def show_question_one(self):
        if self.ids.img.height == dp(0):
            self.ids.img.height = dp(300)
            self.ids.img.width = dp(110)
                      
        else:
            self.ids.img.height = dp(0)

    def show_memo(self):
        if self.ids.memo_img.height == dp(0):
            self.ids.memo_img.height = dp(535)
            self.ids.memo_img.width = dp(400)

            # Add another image
            self.ids.memo_img2.source = "six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An\ones.png"
            self.ids.memo_img2.height = dp(450)
            self.ids.memo_img2.width = dp(400)                 
        
        else:
            self.ids.memo_img.height = dp(0)
            self.ids.memo_img2.height = dp(0)

    def show_question_two(self):
        if self.ids.question_two_img.height == dp(0):
            self.ids.question_two_img.height = dp(180)
            self.ids.question_two_img.width = dp(110)
        
        else:
            self.ids.question_two_img.height = dp(0)

    def show_memo_two(self):
        if self.ids.memo_two_img.height == dp(0):
            self.ids.memo_two_img.height = dp(300)
            self.ids.memo_two_img.width = dp(110)

            # Add another image
            self.ids.memo_two_img2.source = "six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An/twos.png"
            self.ids.memo_two_img2.height = dp(280)
            self.ids.memo_two_img2.width = dp(110)

        else:
            self.ids.memo_two_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_two_img2.height = dp(0)

    def show_question_three(self):
        if self.ids.question_three_img.height == dp(0):
            self.ids.question_three_img.height = dp(240)
            self.ids.question_three_img.width = dp(110)
        
        else:
            self.ids.question_three_img.height = dp(0)

    def show_memo_three(self):
        if self.ids.memo_three_img.height == dp(0):
            self.ids.memo_three_img.height = dp(535)
            self.ids.memo_three_img.width = dp(410)

        else:
            self.ids.memo_three_img.height = dp(0)

    def show_question_four(self):
        if self.ids.question_four_img.height == dp(0):
            self.ids.question_four_img.height = dp(535)
            self.ids.question_four_img.width = dp(410)

            self.ids.question_four_img2.source = "six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper/fours.png"
            self.ids.question_four_img2.height = dp(535)
            self.ids.question_four_img2.width = dp(410)
        
        else:
            self.ids.question_four_img.height = dp(0)
            self.ids.question_four_img2.height = dp(0)            

    def show_memo_four(self):
        if self.ids.memo_four_img.height == dp(0):
            self.ids.memo_four_img.height = dp(535)
            self.ids.memo_four_img.width = dp(400)

        else:
            self.ids.memo_four_img.height = dp(0)        

    def show_question_five(self):
        if self.ids.question_five_img.height == dp(0):
            self.ids.question_five_img.height = dp(535)
            self.ids.question_five_img.width = dp(400)
        
        else:
            self.ids.question_five_img.height = dp(0)

    def show_memo_five(self):
        if self.ids.memo_five_img.height == dp(0):
            self.ids.memo_five_img.height = dp(535)
            self.ids.memo_five_img.width = dp(400)

            # Add another image
            self.ids.memo_fives_img2.source = "six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An/fives.png"
            self.ids.memo_fives_img2.height = dp(535)
            self.ids.memo_fives_img2.width = dp(400)

        else:
            self.ids.memo_five_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_fives_img2.height = dp(0)        

    def show_question_six(self):
        if self.ids.question_six_img.height == dp(0):
            self.ids.question_six_img.height = dp(535)
            self.ids.question_six_img.width = dp(400)
        
        else:
            self.ids.question_six_img.height = dp(0)

    def show_memo_six(self):
        if self.ids.memo_six_img.height == dp(0):
            self.ids.memo_six_img.height = dp(350)
            self.ids.memo_six_img.width = dp(110)

            # Add another image
            self.ids.memo_sixs_img2.source = "six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An\sixs.png"
            self.ids.memo_sixs_img2.height = dp(535)
            self.ids.memo_sixs_img2.width = dp(410)

        else:
            self.ids.memo_six_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_sixs_img2.height = dp(0)

    def show_question_seven(self):
        if self.ids.question_seven_img.height == dp(0):
            self.ids.question_seven_img.height = dp(335)
            self.ids.question_seven_img.width = dp(210)
        
        else:
            self.ids.question_seven_img.height = dp(0)
          

    def show_memo_seven(self):
        if self.ids.memo_seven_img.height == dp(0):
            self.ids.memo_seven_img.height = dp(435)
            self.ids.memo_seven_img.width = dp(310)

        else:
            self.ids.memo_seven_img.height = dp(0)

    def show_question_eight(self):
        if self.ids.question_eight_img.height == dp(0):
            self.ids.question_eight_img.height = dp(435)
            self.ids.question_eight_img.width = dp(310)

            self.ids.question_eights_img2.source = "six\Grade 12 SC Mathematics P1-30121 (SG) Supplementary 2006 Question Paper/eights.png"
            self.ids.question_eights_img2.height = dp(535)
            self.ids.question_eights_img2.width = dp(410)
        
        else:
            self.ids.question_eight_img.height = dp(0)
            self.ids.question_eights_img2.height = dp(0)            

    def show_memo_eight(self):
        if self.ids.memo_eight_img.height == dp(0):
            self.ids.memo_eight_img.height = dp(435)
            self.ids.memo_eight_img.width = dp(300)

            # Add another image
            self.ids.memo_eights_img2.source = "six\Grade 12 SC Mathematics P1 (SG) (English) Supplementary 2006 Possible An/eights.png"
            self.ids.memo_eights_img2.height = dp(535)
            self.ids.memo_eights_img2.width = dp(400)

        else:
            self.ids.memo_eight_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_eights_img2.height = dp(0)

    def show_formula_sheet(self):
        if self.ids.formula_sheet_img.height == dp(0):
            self.ids.formula_sheet_img.height = dp(535)
            self.ids.formula_sheet_img.width = dp(400)
        
        else:
            self.ids.formula_sheet_img.height = dp(0)

class Six_March_February_Paper_Two_SG_Screen(Screen):

    def show_question_one(self):
        if self.ids.img.height == dp(0):
            self.ids.img.height = dp(530)
            self.ids.img.width = dp(410)
                      
        else:
            self.ids.img.height = dp(0)
    
    def show_memo(self):
        if self.ids.memo_img.height == dp(0):
            self.ids.memo_img.height = dp(535)
            self.ids.memo_img.width = dp(400)

            # Add another image
            self.ids.memo_img2.source = "six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\ones.png"
            self.ids.memo_img2.height = dp(535)
            self.ids.memo_img2.width = dp(400)                 
            # Add another image
            self.ids.memo_img3.source = "six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\oness.png"
            self.ids.memo_img3.height = dp(535)
            self.ids.memo_img3.width = dp(400)
            # Add another image
            self.ids.memo_img4.source = "six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\onesss.png"
            self.ids.memo_img4.height = dp(535)
            self.ids.memo_img4.width = dp(400)
            # Add another image
            self.ids.memo_img5.source = "six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\onesss.png"
            self.ids.memo_img5.height = dp(535)
            self.ids.memo_img5.width = dp(400)

        else:
            self.ids.memo_img.height = dp(0)
            self.ids.memo_img2.height = dp(0)
            self.ids.memo_img3.height = dp(0)
            self.ids.memo_img4.height = dp(0)
            self.ids.memo_img5.height = dp(0)

    def show_question_two(self):
        if self.ids.question_two_img.height == dp(0):
            self.ids.question_two_img.height = dp(535)
            self.ids.question_two_img.width = dp(400)
        
        else:
            self.ids.question_two_img.height = dp(0)

    def show_memo_two(self):
        if self.ids.memo_two_img.height == dp(0):
            self.ids.memo_two_img.height = dp(535)
            self.ids.memo_two_img.width = dp(400)

        else:
            self.ids.memo_two_img.height = dp(0)

    def show_question_three(self):
        if self.ids.question_three_img.height == dp(0):
            self.ids.question_three_img.height = dp(535)
            self.ids.question_three_img.width = dp(400)
        
        else:
            self.ids.question_three_img.height = dp(0)

    def show_memo_three(self):
        if self.ids.memo_three_img.height == dp(0):
            self.ids.memo_three_img.height = dp(535)
            self.ids.memo_three_img.width = dp(410)

        else:
            self.ids.memo_three_img.height = dp(0)

    def show_question_four(self):
        if self.ids.question_four_img.height == dp(0):
            self.ids.question_four_img.height = dp(435)
            self.ids.question_four_img.width = dp(300)
        
        else:
            self.ids.question_four_img.height = dp(0)            

    def show_memo_four(self):
        if self.ids.memo_four_img.height == dp(0):
            self.ids.memo_four_img.height = dp(535)
            self.ids.memo_four_img.width = dp(400)

        else:
            self.ids.memo_four_img.height = dp(0) 

    def show_question_five(self):
        if self.ids.question_five_img.height == dp(0):
            self.ids.question_five_img.height = dp(450)
            self.ids.question_five_img.width = dp(350)
        
        else:
            self.ids.question_five_img.height = dp(0)

    def show_memo_five(self):
        if self.ids.memo_five_img.height == dp(0):
            self.ids.memo_five_img.height = dp(535)
            self.ids.memo_five_img.width = dp(400)

        else:
            self.ids.memo_five_img.height = dp(0)

    def show_question_six(self):
        if self.ids.question_six_img.height == dp(0):
            self.ids.question_six_img.height = dp(535)
            self.ids.question_six_img.width = dp(400)
        
        else:
            self.ids.question_six_img.height = dp(0)

    def show_memo_six(self):
        if self.ids.memo_six_img.height == dp(0):
            self.ids.memo_six_img.height = dp(535)
            self.ids.memo_six_img.width = dp(400)

        else:
            self.ids.memo_six_img.height = dp(0)

    def show_question_seven(self):
        if self.ids.question_seven_img.height == dp(0):
            self.ids.question_seven_img.height = dp(535)
            self.ids.question_seven_img.width = dp(400)

            # Add another image
            self.ids.question_seven_img2.source = "six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper\sevens.png"
            self.ids.question_seven_img2.height = dp(535)
            self.ids.question_seven_img2.width = dp(400)
        
        else:
            self.ids.question_seven_img.height = dp(0)
            self.ids.question_seven_img2.height = dp(0)
          

    def show_memo_seven(self):
        if self.ids.memo_seven_img.height == dp(0):
            self.ids.memo_seven_img.height = dp(535)
            self.ids.memo_seven_img.width = dp(400)

            # Add another image
            self.ids.memo_sevens_img2.source = "six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers\sevens.png"
            self.ids.memo_sevens_img2.height = dp(535)
            self.ids.memo_sevens_img2.width = dp(400)

        else:
            self.ids.memo_seven_img.height = dp(0)
            self.ids.memo_sevens_img2.height = dp(0)

    def show_question_eight(self):
        if self.ids.question_eight_img.height == dp(0):
            self.ids.question_eight_img.height = dp(535)
            self.ids.question_eight_img.width = dp(400)
        
        else:
            self.ids.question_eight_img.height = dp(0)           

    def show_memo_eight(self):
        if self.ids.memo_eight_img.height == dp(0):
            self.ids.memo_eight_img.height = dp(535)
            self.ids.memo_eight_img.width = dp(400)

        else:
            self.ids.memo_eight_img.height = dp(0)

    def show_question_nine(self):
        if self.ids.question_nine_img.height == dp(0):
            self.ids.question_nine_img.height = dp(535)
            self.ids.question_nine_img.width = dp(400)

            self.ids.question_nine_img2.source = "six\paper 2 SG\Grade 12 SC Mathematics P2-30122 (SG) Supplementary 2006 Question Paper/nines.png"
            self.ids.question_nine_img2.height = dp(535)
            self.ids.question_nine_img2.width = dp(400)
        
        else:
            self.ids.question_nine_img.height = dp(0)
            self.ids.question_nine_img2.height = dp(0)            

    def show_memo_nine(self):
        if self.ids.memo_nine_img.height == dp(0):
            self.ids.memo_nine_img.height = dp(535)
            self.ids.memo_nine_img.width = dp(400)

            # Add another image
            self.ids.memo_nine_img2.source = "six\paper 2 SG\Grade 12 SC Mathematics P2 (SG) Supplementary 2006 Possible Answers/nines.png"
            self.ids.memo_nine_img2.height = dp(535)
            self.ids.memo_nine_img2.width = dp(400)

        else:
            self.ids.memo_nine_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_nine_img2.height = dp(0)

    def show_formula_sheet(self):
        if self.ids.formula_sheet_img.height == dp(0):
            self.ids.formula_sheet_img.height = dp(535)
            self.ids.formula_sheet_img.width = dp(400)
        
        else:
            self.ids.formula_sheet_img.height = dp(0)

class Six_March_February_Paper_One_HG_Screen(Screen):

    def show_question_one(self):
        if self.ids.img.height == dp(0):
            self.ids.img.height = dp(535)
            self.ids.img.width = dp(410)
                      
        else:
            self.ids.img.height = dp(0)

    def show_memo(self):
        if self.ids.memo_img.height == dp(0):
            self.ids.memo_img.height = dp(535)
            self.ids.memo_img.width = dp(400)

            # Add another image
            self.ids.memo_img2.source = "six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/ones.png"
            self.ids.memo_img2.height = dp(535)
            self.ids.memo_img2.width = dp(400)                 

            # Add another image
            self.ids.memo_img3.source = "six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/oness.png"
            self.ids.memo_img3.height = dp(535)
            self.ids.memo_img3.width = dp(400) 

        else:
            self.ids.memo_img.height = dp(0)
            self.ids.memo_img2.height = dp(0)
            self.ids.memo_img3.height = dp(0)

    def show_question_two(self):
        if self.ids.question_two_img.height == dp(0):
            self.ids.question_two_img.height = dp(535)
            self.ids.question_two_img.width = dp(410)

            self.ids.question_two_img2.source = "six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)/twos.png"
            self.ids.question_two_img2.height = dp(535)
            self.ids.question_two_img2.width = dp(410) 

        else:
            self.ids.question_two_img.height = dp(0)
            self.ids.question_two_img2.height = dp(0)

    def show_memo_two(self):
        if self.ids.memo_two_img.height == dp(0):
            self.ids.memo_two_img.height = dp(535)
            self.ids.memo_two_img.width = dp(410)

            # Add another image
            self.ids.memo_two_img2.source = "six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/twos.png"
            self.ids.memo_two_img2.height = dp(535)
            self.ids.memo_two_img2.width = dp(410)

        else:
            self.ids.memo_two_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_two_img2.height = dp(0)

    def show_question_three(self):
        if self.ids.question_three_img.height == dp(0):
            self.ids.question_three_img.height = dp(240)
            self.ids.question_three_img.width = dp(110)
        
        else:
            self.ids.question_three_img.height = dp(0)

    def show_memo_three(self):
        if self.ids.memo_three_img.height == dp(0):
            self.ids.memo_three_img.height = dp(335)
            self.ids.memo_three_img.width = dp(110)

        else:
            self.ids.memo_three_img.height = dp(0)

    def show_question_four(self):
        if self.ids.question_four_img.height == dp(0):
            self.ids.question_four_img.height = dp(335)
            self.ids.question_four_img.width = dp(110)
        
        else:
            self.ids.question_four_img.height = dp(0)
                    

    def show_memo_four(self):
        if self.ids.memo_four_img.height == dp(0):
            self.ids.memo_four_img.height = dp(235)
            self.ids.memo_four_img.width = dp(110)

            self.ids.memo_four_img2.source = "six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/fours.png"
            self.ids.memo_four_img2.height = dp(535)
            self.ids.memo_four_img2.width = dp(410)

        else:
            self.ids.memo_four_img.height = dp(0)
            self.ids.memo_four_img2.height = dp(0)

    def show_question_five(self):
        if self.ids.question_five_img.height == dp(0):
            self.ids.question_five_img.height = dp(235)
            self.ids.question_five_img.width = dp(110)

            # Add another image
            self.ids.question_fives_img2.source = "six\paper 1 HG\Grade 12 SC Mathematics P1-30111 (HG) Supplementary 2006 Question Paper  (2)/fives.png"
            self.ids.question_fives_img2.height = dp(235)
            self.ids.question_fives_img2.width = dp(110)

        else:
            self.ids.question_five_img.height = dp(0)
            self.ids.question_fives_img2.height = dp(0)

    def show_memo_five(self):
        if self.ids.memo_five_img.height == dp(0):
            self.ids.memo_five_img.height = dp(535)
            self.ids.memo_five_img.width = dp(410)

            # Add another image
            self.ids.memo_fives_img2.source = "six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/fives.png"
            self.ids.memo_fives_img2.height = dp(335)
            self.ids.memo_fives_img2.width = dp(110)

        else:
            self.ids.memo_five_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_fives_img2.height = dp(0) 

    def show_question_six(self):
        if self.ids.question_six_img.height == dp(0):
            self.ids.question_six_img.height = dp(335)
            self.ids.question_six_img.width = dp(110)
        
        else:
            self.ids.question_six_img.height = dp(0)

    def show_memo_six(self):
        if self.ids.memo_six_img.height == dp(0):
            self.ids.memo_six_img.height = dp(335)
            self.ids.memo_six_img.width = dp(110)

            # Add another image
            self.ids.memo_six_img2.source = "six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers\sixs.png"
            self.ids.memo_six_img2.height = dp(335)
            self.ids.memo_six_img2.width = dp(110)

        else:
            self.ids.memo_six_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_six_img2.height = dp(0)

    def show_question_seven(self):
        if self.ids.question_seven_img.height == dp(0):
            self.ids.question_seven_img.height = dp(535)
            self.ids.question_seven_img.width = dp(410)

        else:
            self.ids.question_seven_img.height = dp(0)    

    def show_memo_seven(self):
        if self.ids.memo_seven_img.height == dp(0):
            self.ids.memo_seven_img.height = dp(335)
            self.ids.memo_seven_img.width = dp(110)

            # Add another image
            self.ids.memo_sevens_img2.source = "six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers\sevens.png"
            self.ids.memo_sevens_img2.height = dp(535)
            self.ids.memo_sevens_img2.width = dp(410)

        else:
            self.ids.memo_seven_img.height = dp(0)
            self.ids.memo_sevens_img2.height = dp(0)

    def show_question_eight(self):
        if self.ids.question_eight_img.height == dp(0):
            self.ids.question_eight_img.height = dp(535)
            self.ids.question_eight_img.width = dp(410)
        
        else:
            self.ids.question_eight_img.height = dp(0)
                       

    def show_memo_eight(self):
        if self.ids.memo_eight_img.height == dp(0):
            self.ids.memo_eight_img.height = dp(535)
            self.ids.memo_eight_img.width = dp(410)

        else:
            self.ids.memo_eight_img.height = dp(0)

    def show_formula_sheet(self):
        if self.ids.formula_sheet_img.height == dp(0):
            self.ids.formula_sheet_img.height = dp(535)
            self.ids.formula_sheet_img.width = dp(400)
        
        else:
            self.ids.formula_sheet_img.height = dp(0)

class Six_March_February_Paper_Two_HG_Screen(Screen):

    def show_question_one(self):
        if self.ids.img.height == dp(0):
            self.ids.img.height = dp(530)
            self.ids.img.width = dp(410)
                      
        else:
            self.ids.img.height = dp(0)
    
    def show_memo(self):
        if self.ids.memo_img.height == dp(0):
            self.ids.memo_img.height = dp(535)
            self.ids.memo_img.width = dp(410)

            # Add another image
            self.ids.memo_img2.source = "six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\ones.png"
            self.ids.memo_img2.height = dp(535)
            self.ids.memo_img2.width = dp(410)                 
            # Add another image
            self.ids.memo_img3.source = "six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\oness.png"
            self.ids.memo_img3.height = dp(535)
            self.ids.memo_img3.width = dp(410)

        else:
            self.ids.memo_img.height = dp(0)
            self.ids.memo_img2.height = dp(0)
            self.ids.memo_img3.height = dp(0)

    def show_question_two(self):
        if self.ids.question_two_img.height == dp(0):
            self.ids.question_two_img.height = dp(535)
            self.ids.question_two_img.width = dp(410)
        
        else:
            self.ids.question_two_img.height = dp(0)

    def show_memo_two(self):
        if self.ids.memo_two_img.height == dp(0):
            self.ids.memo_two_img.height = dp(535)
            self.ids.memo_two_img.width = dp(410)

            # Add another image
            self.ids.memo_two_img2.source = "six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/twos.png"
            self.ids.memo_two_img2.height = dp(535)
            self.ids.memo_two_img2.width = dp(410)

            self.ids.memo_two_img3.source = "six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/twoss.png"
            self.ids.memo_two_img3.height = dp(535)
            self.ids.memo_two_img3.width = dp(410)

        else:
            self.ids.memo_two_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_two_img2.height = dp(0)
            self.ids.memo_two_img3.height = dp(0)

    def show_question_three(self):
        if self.ids.question_three_img.height == dp(0):
            self.ids.question_three_img.height = dp(240)
            self.ids.question_three_img.width = dp(110)
        
        else:
            self.ids.question_three_img.height = dp(0)

    def show_memo_three(self):
        if self.ids.memo_three_img.height == dp(0):
            self.ids.memo_three_img.height = dp(535)
            self.ids.memo_three_img.width = dp(410)

        else:
            self.ids.memo_three_img.height = dp(0)

    def show_question_four(self):
        if self.ids.question_four_img.height == dp(0):
            self.ids.question_four_img.height = dp(335)
            self.ids.question_four_img.width = dp(110)
        
        else:
            self.ids.question_four_img.height = dp(0)
                    

    def show_memo_four(self):
        if self.ids.memo_four_img.height == dp(0):
            self.ids.memo_four_img.height = dp(535)
            self.ids.memo_four_img.width = dp(410)

            self.ids.memo_four_img2.source = "six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/fours.png"
            self.ids.memo_four_img2.height = dp(535)
            self.ids.memo_four_img2.width = dp(410)

        else:
            self.ids.memo_four_img.height = dp(0)
            self.ids.memo_four_img2.height = dp(0)

    def show_question_five(self):
        if self.ids.question_five_img.height == dp(0):
            self.ids.question_five_img.height = dp(335)
            self.ids.question_five_img.width = dp(110)
        
        else:
            self.ids.question_five_img.height = dp(0)

    def show_memo_five(self):
        if self.ids.memo_five_img.height == dp(0):
            self.ids.memo_five_img.height = dp(535)
            self.ids.memo_five_img.width = dp(410)

        else:
            self.ids.memo_five_img.height = dp(0)

    def show_question_six(self):
        if self.ids.question_six_img.height == dp(0):
            self.ids.question_six_img.height = dp(435)
            self.ids.question_six_img.width = dp(310)

            self.ids.question_six_img2.source = "six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)\sixs.png"
            self.ids.question_six_img2.height = dp(535)
            self.ids.question_six_img2.width = dp(410)
        
        else:
            self.ids.question_six_img.height = dp(0)
            self.ids.question_six_img2.height = dp(0)

    def show_memo_six(self):
        if self.ids.memo_six_img.height == dp(0):
            self.ids.memo_six_img.height = dp(535)
            self.ids.memo_six_img.width = dp(410)

            # Add another image
            self.ids.memo_six_img2.source = "six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\sixs.png"
            self.ids.memo_six_img2.height = dp(535)
            self.ids.memo_six_img2.width = dp(410)

            # Add another image
            self.ids.memo_six_img3.source = "six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\sixss.png"
            self.ids.memo_six_img3.height = dp(435)
            self.ids.memo_six_img3.width = dp(310)

        else:
            self.ids.memo_six_img.height = dp(0)
            self.ids.memo_six_img2.height = dp(0)
            self.ids.memo_six_img3.height = dp(0)

    def show_question_seven(self):
        if self.ids.question_seven_img.height == dp(0):
            self.ids.question_seven_img.height = dp(335)
            self.ids.question_seven_img.width = dp(110)
        
        else:
            self.ids.question_seven_img.height = dp(0)

    def show_memo_seven(self):
        if self.ids.memo_seven_img.height == dp(0):
            self.ids.memo_seven_img.height = dp(335)
            self.ids.memo_seven_img.width = dp(110)

        else:
            self.ids.memo_seven_img.height = dp(0)

    def show_question_eight(self):
        if self.ids.question_eight_img.height == dp(0):
            self.ids.question_eight_img.height = dp(335)
            self.ids.question_eight_img.width = dp(110)

            self.ids.question_eight_img2.source = "six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)\eights.png"
            self.ids.question_eight_img2.height = dp(535)
            self.ids.question_eight_img2.width = dp(410)
        
        else:
            self.ids.question_eight_img.height = dp(0)
            self.ids.question_eight_img2.height = dp(0)

    def show_memo_eight(self):
        if self.ids.memo_eight_img.height == dp(0):
            self.ids.memo_eight_img.height = dp(535)
            self.ids.memo_eight_img.width = dp(410)

            # Add another image
            self.ids.memo_eight_img2.source = "six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers\eights.png"
            self.ids.memo_eight_img2.height = dp(535)
            self.ids.memo_eight_img2.width = dp(410)

        else:
            self.ids.memo_eight_img.height = dp(0)
            self.ids.memo_eight_img2.height = dp(0)

    def show_question_nine(self):
        if self.ids.question_nine_img.height == dp(0):
            self.ids.question_nine_img.height = dp(335)
            self.ids.question_nine_img.width = dp(110)
        
        else:
            self.ids.question_nine_img.height = dp(0)

    def show_memo_nine(self):
        if self.ids.memo_nine_img.height == dp(0):
            self.ids.memo_nine_img.height = dp(535)
            self.ids.memo_nine_img.width = dp(410)

            # Add another image
            self.ids.memo_nine_img2.source = "six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/nines.png"
            self.ids.memo_nine_img2.height = dp(535)
            self.ids.memo_nine_img2.width = dp(410)

        else:
            self.ids.memo_nine_img.height = dp(0)
            self.ids.memo_nine_img2.height = dp(0)            

    def show_question_ten(self):
        if self.ids.question_ten_img.height == dp(0):
            self.ids.question_ten_img.height = dp(335)
            self.ids.question_ten_img.width = dp(110)

            self.ids.question_ten_img2.source = "six\paper 2 HG\Grade 12 SC Mathematics P2-30112 (HG) Supplementary 2006 Question Paper  (2)/tens.png"
            self.ids.question_ten_img2.height = dp(535)
            self.ids.question_ten_img2.width = dp(410)
        
        else:
            self.ids.question_ten_img.height = dp(0)
            self.ids.question_ten_img2.height = dp(0)

    def show_memo_ten(self):
        if self.ids.memo_ten_img.height == dp(0):
            self.ids.memo_ten_img.height = dp(535)
            self.ids.memo_ten_img.width = dp(410)

            # Add another image
            self.ids.memo_ten_img2.source = "six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/tens.png"
            self.ids.memo_ten_img2.height = dp(535)
            self.ids.memo_ten_img2.width = dp(410)

            # Add another image
            self.ids.memo_ten_img3.source = "six\paper 2 HG\Grade 12 SC Mathematics P2 (HG) Supplementary 2006 Possible Answers/tenss.png"
            self.ids.memo_ten_img3.height = dp(535)
            self.ids.memo_ten_img3.width = dp(410)

        else:
            self.ids.memo_ten_img.height = dp(0)
            self.ids.memo_ten_img2.height = dp(0)
            self.ids.memo_ten_img3.height = dp(0)

    def show_formula_sheet(self):
        if self.ids.formula_sheet_img.height == dp(0):
            self.ids.formula_sheet_img.height = dp(535)
            self.ids.formula_sheet_img.width = dp(400)
        
        else:
            self.ids.formula_sheet_img.height = dp(0)

class Six_November_Screen(Screen): 
    pass

class Six_November_Paper_One_HG_Screen(Screen):

    def show_question_one(self):
        if self.ids.img.height == dp(0):
            self.ids.img.height = dp(535)
            self.ids.img.width = dp(410)
                      
        else:
            self.ids.img.height = dp(0)

    def show_memo(self):
        if self.ids.memo_img.height == dp(0):
            self.ids.memo_img.height = dp(535)
            self.ids.memo_img.width = dp(400)

            # Add another image
            self.ids.memo_img2.source = "six\paper 1 HG\Grade 12 SC Mathematics P1 (HG) Supplementary 2006 Possible Answers/ones.png"
            self.ids.memo_img2.height = dp(535)
            self.ids.memo_img2.width = dp(400)                 

            # Add another image
            self.ids.memo_img3.source = "six/November/paper 1 HG/November 2006 Possible Answers/ones.png"
            self.ids.memo_img3.height = dp(535)
            self.ids.memo_img3.width = dp(400) 

            # Add another image
            self.ids.memo_img4.source = "six/November/paper 1 HG/November 2006 Possible Answers/onesss.png"
            self.ids.memo_img4.height = dp(535)
            self.ids.memo_img4.width = dp(400)                 

            # Add another image
            self.ids.memo_img5.source = "six/November/paper 1 HG/November 2006 Possible Answers/onessss.png"
            self.ids.memo_img5.height = dp(235)
            self.ids.memo_img5.width = dp(110) 

        else:
            self.ids.memo_img.height = dp(0)
            self.ids.memo_img2.height = dp(0)
            self.ids.memo_img3.height = dp(0)
            self.ids.memo_img4.height = dp(0)
            self.ids.memo_img5.height = dp(0)

    def show_question_two(self):
        if self.ids.question_two_img.height == dp(0):
            self.ids.question_two_img.height = dp(535)
            self.ids.question_two_img.width = dp(410)

            self.ids.question_two_img2.source = "six/November/paper 1 HG/November 2006 Question Paper/twos.png"
            self.ids.question_two_img2.height = dp(335)
            self.ids.question_two_img2.width = dp(210)
        
        else:
            self.ids.question_two_img.height = dp(0)
            self.ids.question_two_img2.height = dp(0)

    def show_memo_two(self):
        if self.ids.memo_two_img.height == dp(0):
            self.ids.memo_two_img.height = dp(535)
            self.ids.memo_two_img.width = dp(410)

            # Add another image
            self.ids.memo_two_img2.source = "six/November/paper 1 HG/November 2006 Possible Answers/twoss.png"
            self.ids.memo_two_img2.height = dp(535)
            self.ids.memo_two_img2.width = dp(410)

            self.ids.memo_two_img3.source = "six/November/paper 1 HG/November 2006 Possible Answers/twosss.png"
            self.ids.memo_two_img3.height = dp(535)
            self.ids.memo_two_img3.width = dp(410)

            self.ids.memo_two_img4.source = "six/November/paper 1 HG/November 2006 Possible Answers/twossss.png"
            self.ids.memo_two_img4.height = dp(535)
            self.ids.memo_two_img4.width = dp(410)

        else:
            self.ids.memo_two_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_two_img2.height = dp(0)
            self.ids.memo_two_img3.height = dp(0)
            self.ids.memo_two_img4.height = dp(0)

    def show_question_three(self):
        if self.ids.question_three_img.height == dp(0):
            self.ids.question_three_img.height = dp(210)
            self.ids.question_three_img.width = dp(90)
        
        else:
            self.ids.question_three_img.height = dp(0)

    def show_memo_three(self):
        if self.ids.memo_three_img.height == dp(0):
            self.ids.memo_three_img.height = dp(535)
            self.ids.memo_three_img.width = dp(410)

            # Add another image
            self.ids.memo_three_img2.source = "six/November/paper 1 HG/November 2006 Possible Answers/threes.png"
            self.ids.memo_three_img2.height = dp(535)
            self.ids.memo_three_img2.width = dp(410)

        else:
            self.ids.memo_three_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_three_img2.height = dp(0)

    def show_question_four(self):
        if self.ids.question_four_img.height == dp(0):
            self.ids.question_four_img.height = dp(535)
            self.ids.question_four_img.width = dp(410)
        
        else:
            self.ids.question_four_img.height = dp(0)

    def show_memo_four(self):
        if self.ids.memo_four_img.height == dp(0):
            self.ids.memo_four_img.height = dp(535)
            self.ids.memo_four_img.width = dp(410)

            # Add another image
            self.ids.memo_four_img2.source = "six/November/paper 1 HG/November 2006 Possible Answers/fours.png"
            self.ids.memo_four_img2.height = dp(535)
            self.ids.memo_four_img2.width = dp(410)

        else:
            self.ids.memo_four_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_four_img2.height = dp(0)

    def show_question_five(self):
        if self.ids.question_five_img.height == dp(0):
            self.ids.question_five_img.height = dp(535)
            self.ids.question_five_img.width = dp(410)
        
        else:
            self.ids.question_five_img.height = dp(0)

    def show_memo_five(self):
        if self.ids.memo_five_img.height == dp(0):
            self.ids.memo_five_img.height = dp(535)
            self.ids.memo_five_img.width = dp(410)

            # Add another image
            self.ids.memo_five_img2.source = "six/November/paper 1 HG/November 2006 Possible Answers/fives.png"
            self.ids.memo_five_img2.height = dp(535)
            self.ids.memo_five_img2.width = dp(410)

            # Add another image
            self.ids.memo_five_img3.source = "six/November/paper 1 HG/November 2006 Possible Answers/fivess.png"
            self.ids.memo_five_img3.height = dp(535)
            self.ids.memo_five_img3.width = dp(410)

            # Add another image
            self.ids.memo_five_img4.source = "six/November/paper 1 HG/November 2006 Possible Answers/fivesss.png"
            self.ids.memo_five_img4.height = dp(535)
            self.ids.memo_five_img4.width = dp(410)

        else:
            self.ids.memo_five_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_five_img2.height = dp(0)
            self.ids.memo_five_img3.height = dp(0)
            self.ids.memo_five_img4.height = dp(0)

    def show_question_six(self):
        if self.ids.question_six_img.height == dp(0):
            self.ids.question_six_img.height = dp(535)
            self.ids.question_six_img.width = dp(410)
        
        else:
            self.ids.question_six_img.height = dp(0)

    def show_memo_six(self):
        if self.ids.memo_six_img.height == dp(0):
            self.ids.memo_six_img.height = dp(535)
            self.ids.memo_six_img.width = dp(410)

            # Add another image
            self.ids.memo_six_img2.source = "six/November/paper 1 HG/November 2006 Possible Answers/sixs.png"
            self.ids.memo_six_img2.height = dp(535)
            self.ids.memo_six_img2.width = dp(410)

        else:
            self.ids.memo_six_img.height = dp(0)
            # Hide the second image when hiding the first one
            self.ids.memo_six_img2.height = dp(0)

    def show_question_seven(self):
        if self.ids.question_seven_img.height == dp(0):
            self.ids.question_seven_img.height = dp(535)
            self.ids.question_seven_img.width = dp(410)
        
        else:
            self.ids.question_seven_img.height = dp(0)

    def show_memo_seven(self):
        if self.ids.memo_seven_img.height == dp(0):
            self.ids.memo_seven_img.height = dp(535)
            self.ids.memo_seven_img.width = dp(410)

        else:
            self.ids.memo_seven_img.height = dp(0)

    def show_question_eight(self):
        if self.ids.question_eight_img.height == dp(0):
            self.ids.question_eight_img.height = dp(535)
            self.ids.question_eight_img.width = dp(410)
        
        else:
            self.ids.question_eight_img.height = dp(0)

    def show_formula_sheet(self):
        if self.ids.formula_sheet_img.height == dp(0):
            self.ids.formula_sheet_img.height = dp(535)
            self.ids.formula_sheet_img.width = dp(400)
        
        else:
            self.ids.formula_sheet_img.height = dp(0)

class Six_November_Paper_Two_HG_Screen(Screen):

    def show_question_one(self):
        if self.ids.img.height == dp(0):
            self.ids.img.height = dp(535)
            self.ids.img.width = dp(410)
                      
        else:
            self.ids.img.height = dp(0)

    def show_memo(self):
        if self.ids.memo_img.height == dp(0):
            self.ids.memo_img.height = dp(535)
            self.ids.memo_img.width = dp(400)

            # Add another image
            self.ids.memo_img2.source = "six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/one.png"
            self.ids.memo_img2.height = dp(535)
            self.ids.memo_img2.width = dp(400)                 

            # Add another image
            self.ids.memo_img3.source = "six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/oness.png"
            self.ids.memo_img3.height = dp(535)
            self.ids.memo_img3.width = dp(400) 

            # Add another image
            self.ids.memo_img4.source = "six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/onesss.png"
            self.ids.memo_img4.height = dp(535)
            self.ids.memo_img4.width = dp(400)                 

        else:
            self.ids.memo_img.height = dp(0)
            self.ids.memo_img2.height = dp(0)
            self.ids.memo_img3.height = dp(0)
            self.ids.memo_img4.height = dp(0)
            
    def show_question_two(self):
        if self.ids.question_two_img.height == dp(0):
            self.ids.question_two_img.height = dp(535)
            self.ids.question_two_img.width = dp(410)
        
        else:
            self.ids.question_two_img.height = dp(0)
            
    def show_memo(self):
        if self.ids.memo_img.height == dp(0):
            self.ids.memo_img.height = dp(435)
            self.ids.memo_img.width = dp(300)

            # Add another image
            self.ids.memo_two_img2.source = "six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/twos.png"
            self.ids.memo_two_img2.height = dp(535)
            self.ids.memo_two_img2.width = dp(400)                 

            # Add another image
            self.ids.memo_two_img3.source = "six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/twoss.png"
            self.ids.memo_two_img3.height = dp(535)
            self.ids.memo_two_img3.width = dp(400) 

            # Add another image
            self.ids.memo_two_img4.source = "six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/twosss.png"
            self.ids.memo_two_img4.height = dp(535)
            self.ids.memo_two_img4.width = dp(400)
            
            # Add another image
            self.ids.memo_two_img5.source = "six/November/paper 2 HG/Grade 12 SC Mathematics (HG) P2 November 2006 Possible Answers/twossss.png"
            self.ids.memo_two_img5.height = dp(535)
            self.ids.memo_two_img5.width = dp(400)                  

        else:
            self.ids.memo_two_img.height = dp(0)
            self.ids.memo_two_img2.height = dp(0)
            self.ids.memo_two_img3.height = dp(0)
            self.ids.memo_two_img4.height = dp(0)
            self.ids.memo_two_img5.height = dp(0)
            

class Study_Map_Home(App):
	
    def build(self):
        self.title = "Study_Map"
        #self.theme_cls.primary_palette = "LightGreen"
        self.manager = Builder.load_string(home_of_kv)
        return self.manager  

if __name__ == "__main__":
    Window.size = (360,640)
    Study_Map_Home().run()