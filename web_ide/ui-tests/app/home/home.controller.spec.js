describe('test home.controller', function () {

    'use strict';

    var ctrl = null,
        $rootScope = null,
        scope = null,
        githubAuthServiceMock = null,
        $window = null,
        expectedUserId = 'testUserId',
        expectedUserLogin = 'testUserLogin';

    beforeEach(module('webIde.home'));

    beforeEach(inject(function ($controller, $q, _$rootScope_) {
        $rootScope = _$rootScope_;

        $rootScope.$user = {
            userId: expectedUserId,
            userLogin: expectedUserLogin
        };

        scope = $rootScope.$new();

        githubAuthServiceMock = {
            deferred: $q.defer(),
            login: function () {
            },
            logout: function () {
            }
        };

        $window = {
            location: {
                href: 'some-url'
            }
        };

        spyOn(githubAuthServiceMock, 'login');
        spyOn(githubAuthServiceMock, 'logout').and.callFake(function () {
            var deferred = $q.defer();
            deferred.resolve('user has logout');
            return deferred.promise;
        });

        ctrl = $controller('homeController', {
            $rootScope: $rootScope,
            $scope: scope,
            $window: $window,
            GithubAuthService: githubAuthServiceMock
        })
    }));

    it('should initialize $scope', function () {

        expect(scope.isUserLoggedIn).toBe(true);
        expect(scope.user.userId).toBe(expectedUserId);
        expect(scope.user.userLogin).toBe(expectedUserLogin);
    });

    it('should call github.auth.service on $scope.login()', function () {

        scope.login();

        expect(githubAuthServiceMock.login).toHaveBeenCalled();
    });

    it('should call github.auth.service on $scope.logout() and redirect user to home page', function () {

        scope.logout();
        $rootScope.$apply();

        expect(githubAuthServiceMock.logout).toHaveBeenCalled();
        expect($window.location.href).toBe('/');
    });
});

