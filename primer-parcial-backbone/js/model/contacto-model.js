/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 * Model que corresponde al recurso contacto.
 */
var ContactoModel = Backbone.Model.extend({
    /**
     * Atributos por defecto del model 
     * @field
     */
    defaults: {
        "id": 0,
        "nombre" : "",
        "apellido":"",
        "alias":"",
        "telefono":0,
        "email":"example@email.com",
        "direccion":"",
        "fechaCreacion":null
    }
});