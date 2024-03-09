import pygame as pg
import pygame_gui as pg_gui

pg.freetype.init()

# Player:
PLAYER_START1 = 1.5, 1.5
PLAYER_START2 = 1.5, 4.5
PLAYER_POS = 1.5, 1.5
KEY_COOLDOWN = 0

# Start_up:
RES = WIDTH, HEIGHT = 800, 800

# GUI: 
BUTTON_SIZE = (100, 50)
STAND_BACK_COL = (107, 107, 107, 1)
THEME_PATH = 'Json_Files/theme_0.json'
MANAGER = pg_gui.UIManager((RES), 'Json_Files/theme_0.json')
        
# HTML Texts for text boxes
# Register and Login Page:
welcome_text = """<p>Welcome to the Memory Processing Tool programme. 

Please press the START button when you want to start the programme. 

If you want to leave the programme press the QUIT button</p>"""

preview_text = """<p>Welcome to the MAZE INFORMATION PAGE<br>
When you click the CONTINUE BUTTON you will be presented with a visual puzzle or MAZE. You will be asked to solve the maze puzzle.
1. You will be presented with a maze on the display.
2. A timer will start giving you time to memorise the maze.
3. After the time elapses your task is to move the circle through the maze.
4. The task is complete when you move the circle to the BLACK END SQUARE of the maze.
5. When you complete the maze, you will then be presented with another maze for you to complete.
6. There are 3 mazes in total.
7. When the game ends you will be presented with the results in the form of a graph.</p>

<p>Please click the CONTINUE BUTTON to progress and start the game.</p>"""

login_text = """<p>IF you have used the Memory Processing Tool before, please enter your existing username and password, in the spaces provided on the right to this message, and CLICK the LOGIN button.</p>"""
reg_text = """<p>If this is the first time using the programme, please enter a USERNAME and PASSWORD in the spaces provided on the left to this message.  
No spaces are allowed in the USERNAME and PASSWORD.  
Please enter your age as a whole number.  
After you have completed these two steps, CLICK on the REGISTER button.</p>""" 

# Scatter Graph Page:
graph_text = """<p>Welcome to the GRAPH PAGE.</p>
<p>This page shows you your results in the form of a scatter graph. The graph represents the average time taken and your age and you can see your results against others who have used the tool. 
When you press the START button you will be provided with written feedback about your results.</p>"""

updated_graph_text = """<br><p>Your results should not be seen as being an indication of your processing speed. Results can be affected by such things as anxiety and can vary. If the results indicate that you have a score that is longer than normal you may wish to consult with a medical professional to undertake a more thorough investigation and/or help.</p>"""

vl_risk_h_speed = """<br><p>Very Low Risk, High Processing Speed:
This result indicated that you have a very fast memory processing speed, compared to the average person. This means, compariviely to the average person, you are at little to no risk for any type processing issue such like dimentia.</p>"""

l_risk_a_speed = """<br><p>Low Risk, Average Processing Speed:
This result indicated that you have an average memory processing speed, compared to the average person. This means you are as at risk of any type of a processing issue such like dimentia as the average person.</p>"""

a_risk_s_speed = """<br><p>Slow Processing Speed, Average Risk:
This result indicated that you have a slow processing speed, compared to he average person. This combined with your age means that you are as much at risk of a processing issue as the average indiviual of your age group.</p>"""

l_risk_s_speed = """<br><p>Slow Procesing Speed, Low Risk:
This result indicated that you have a slow processing speed, compared to the average person. This combined with your age means that you are as much at risk of a processing issue as the average indiviual of your age group.</p>
"""

h_risk_vs_speed = """<br><p>Very Slow Processing Speed, High Risk:
This result indicated that you have a very slow processing speed, compared to the average person. This combined with your age means that you are at a high risk of having a memory processing issue like dimentia.</p>)
"""

aa_risk_vs_speed = """<br><p>Very Slow Processing Speed, Above Average Risk:
This result indicated that you have a very slow processing speed, compared to the average person. This combined with your age means that you are at a above average risk of having a memory processing issue like dimentia.</p>"""

# HTML Text Arrays:
TEXT_ARRAY = [preview_text, login_text, reg_text, welcome_text, graph_text, updated_graph_text]
RESULTS_TEXT_ARRAY = [vl_risk_h_speed, l_risk_a_speed, a_risk_s_speed, l_risk_s_speed, h_risk_vs_speed, aa_risk_vs_speed]