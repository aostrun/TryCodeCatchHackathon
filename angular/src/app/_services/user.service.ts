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

    update(blood_type) {
        return this.http.post(apiUrl+'/api/user/change_blood_type/', blood_type);
    }

    delete(id: number) {
        return this.http.delete('/api/users/' + id);
    }

}