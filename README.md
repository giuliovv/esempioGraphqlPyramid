# esempioGraphqlPyramid
Esempio graphene graphql + pyramid.

Inizia installando i requirements (magari in una virtualenv):
```
pip install -r requirements.txt
```

Poi fai andare uscita.py che serve nell'esempio in localhost:8765 ma ti basta modificare la porta.

Per testare lo schema graphql scritto in layerGraohql.py vai su localhost:8765/graph la documentazione di graphene è qua https://graphene-python.org/

L'esempio di pyramid (https://trypyramid.com/) è tratto sputato da qua: https://github.com/graphql-python/webob-graphql

Non ho testato l'esempio in App.js ma l'idea è quella. Molto importante tenere la chiamata a graphql in cima a tutto e poi usare refetch per cambiare i parametri se serve. Graphql ti aggiorna anche la roba come facciamo con firebase.

Comodo perchè puoi modificare front e back quanto ti pare ma lasciando sempre lo schema inalterato quindi senza dover andare avanti e indietro a modificare cose perchè cambiano le API.
