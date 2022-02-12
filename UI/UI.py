from h2o_wave import Q, main, app, ui
import requests

textToAnalyze = ''
analyzedText = ''

@app('/')
async def serve(q: Q):
    global textToAnalyze
    global analyzedText
    
    if q.args.analyze:
        textToAnalyze = q.args.submittedText
        url = 'http://api:5000/' + textToAnalyze
        r = requests.get(url)
        analyzedText = r.text[1:-1]

    # Display a form on the page
    q.page['REM'] = ui.form_card(
        box='1 1 2 4',
        items=[
            ui.text_xl('Enter text to analyze'),
            ui.textbox(name='submittedText', label=''),
            ui.button(name='analyze', label='Analyze'),
            ui.text_xl(analyzedText),
        ],
    )
    
    # Save the page
    await q.page.save()
