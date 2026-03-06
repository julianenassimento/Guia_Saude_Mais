from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

treinos = [
    ("meu plano cobre exame", "cobertura"),
    ("cobre ressonancia", "cobertura"),
    ("tenho direito a cirurgia", "cobertura"),
    ("como funciona reembolso", "reembolso"),
    ("quanto recebo de reembolso", "reembolso"),
    ("tenho carencia", "carencia"),
    ("quanto tempo de carencia", "carencia"),
    ("rede credenciada", "rede"),
    ("quais hospitais atendem", "rede"),
]

frases = [t[0] for t in treinos]
labels = [t[1] for t in treinos]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases)

model = MultinomialNB()
model.fit(X, labels)


def prever_intencao(texto: str) -> str:
    texto_vec = vectorizer.transform([texto.lower()])
    probs = model.predict_proba(texto_vec)[0]
    max_prob = max(probs)

    if max_prob < 0.45:
        return "geral"

    return model.predict(texto_vec)[0]
