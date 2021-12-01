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

def double_pie_chart(df, df2):

    # the same figure for both subplots
    fig = plt.figure(figsize=(8,7))

    def percentage(part,whole):
        return 100 * float(part)/float(whole)

    ax = fig.add_subplot(121)
    positive = format(percentage(df[df['sentiment'] == 1].shape[0],df.shape[0]),'.1f')
    negative = format(percentage(df[df['sentiment'] == 0].shape[0],df.shape[0]),'.1f')

    #Incase of ternary classification or visualizing neutral sentiment
    neutral = format(percentage(df[df['sentiment'] == 2].shape[0],df.shape[0]),'.1f')

    labels = ['Positive ['+str(positive)+'%]','Negative ['+str(negative)+'%]', 
    
    #Incase of ternary classification or visualizing neutral sentiment
    'Neutral ['+str(neutral)+'%]'
    ]   

    sizes = [positive, negative, neutral]
    colors = ['green', 'red', 'gray']
    patches, texts = ax.pie(sizes,colors=colors, startangle=90)
    plt.style.use('default')
    plt.legend(labels)
    plt.axis('equal')
    
    ax = fig.add_subplot(122)
    positive = format(percentage(df2[df2['sentiment'] == 1].shape[0],df2.shape[0]),'.1f')
    negative = format(percentage(df2[df2['sentiment'] == 0].shape[0],df2.shape[0]),'.1f')

    labels = ['Positive ['+str(positive)+'%]','Negative ['+str(negative)+'%]']   

    sizes = [positive, negative]
    colors = ['green', 'red']
    patches, texts = ax.pie(sizes,colors=colors, startangle=90)
    plt.style.use('default')
    plt.legend(labels)


    plt.suptitle("Sentiment Analysis Result for Destiny w/ and w/o Neutral")
    plt.axis('equal')


    plt.show()