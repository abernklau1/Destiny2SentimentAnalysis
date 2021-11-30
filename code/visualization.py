import matplotlib.pyplot as plt


def pie_chart(df_probs):
    def percentage(part,whole):
        return 100 * float(part)/float(whole)

    positive = format(percentage(df_probs[df_probs['sentiment'] == 1].shape[0],df_probs.shape[0]),'.1f')
    negative = format(percentage(df_probs[df_probs['sentiment'] == 0].shape[0],df_probs.shape[0]),'.1f')

    #Incase of ternary classification
    neutral = format(percentage(df_probs[df_probs['sentiment'] == 2].shape[0],df_probs.shape[0]),'.1f')

    labels = ['Positive ['+str(positive)+'%]','Negative ['+str(negative)+'%]', 
    
    #Incase of ternary classification
    'Neutral ['+str(neutral)+'%]'
    ]

    sizes = [positive, negative,
    neutral
    ]
    colors = ['green', 'red', 'gray']
    patches, texts = plt.pie(sizes,colors=colors, startangle=90)
    plt.style.use('default')
    plt.legend(labels)
    plt.title("Sentiment Analysis Result for Destiny" )
    plt.axis('equal')
    return plt.show()