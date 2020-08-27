import { Role } from '../authentication/role';

export class User {
    id: number;
    name: String;
    email: String;
    password: String;
    creationDate?: Date;
    role?: Role;
    token?: string;
}


// export class User {
//     id: number;
//     username: string;
//     password: string;
//     firstName: string;
//     lastName: string;
//     role: Role;
//     token?: string;
// }