import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User, apiUrl } from '../_models';

@Injectable()
export class UserService {
    constructor(private http: HttpClient) { }

    getAll() {
        return this.http.get<User[]>('/api/users');
    }

    getDetails() {
        return this.http.get<User>(apiUrl+'/api/user/user_details/');
    }

    create(user: User) {
        return this.http.post(apiUrl+'/rest-auth/register/', user);
    }

    update(user: User) {
        return this.http.put('/api/users/' + user.user_id, user);
    }

    delete(id: number) {
        return this.http.delete('/api/users/' + id);
    }

}