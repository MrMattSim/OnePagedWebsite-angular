app = angular.module("app", []);

app.controller("AppController", function($http) {
    var app = this;

    $http.get("/api/project").success(function(data) {
        app.projects = data.objects;
    })
});