from flask import Flask,request
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

app = Flask(__name__)
@app.route('/summarize', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        data = request.get_json() 
        original_text = data.get('text')
    
        # Initializing the parser
        my_parser = PlaintextParser.from_string(original_text,Tokenizer('english'))
        # Creating a summary of 3 sentences.
        lex_rank_summarizer = LexRankSummarizer()
        lexrank_summary = lex_rank_summarizer(my_parser.document,sentences_count=3)


        #Generating the summary
        summary = ""
        for sentence in lexrank_summary:
          summary += str(sentence)
        
        return summary
    
    return 'Method Not Allowed'

if __name__ == '__main__':
    app.run()