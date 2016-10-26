/*
*  Collection de personas, para simplificar el ejemplo se utiliza un archivo como
* fuente de datos para simular el GET para obtener los datos.
*/
var ContactoCollection = Backbone.Collection.extend({
    url : 'data/contactos.json',
    model : ContactoModel
});