# 📘 TypeScript Best Practices Knowledge Base

## Overview
This knowledge file contains TypeScript best practices, patterns, and common pitfalls. Reference this when creating TypeScript lessons, reviewing code, or helping with TypeScript questions.

---

## 🎯 Core Principles

### TypeScript Philosophy
- **Type Safety**: Catch errors at compile time
- **Developer Experience**: Better autocomplete and refactoring
- **Gradual Adoption**: Can be added incrementally to JavaScript
- **Structural Typing**: Types based on shape, not name

---

## 📋 Type System Basics

### Primitive Types
```typescript
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;
let nothing: null = null;
let notDefined: undefined = undefined;
```

### Arrays and Tuples
```typescript
// Arrays
let numbers: number[] = [1, 2, 3];
let names: Array<string> = ["Alice", "Bob"];

// Tuples - fixed length, specific types
let person: [string, number] = ["John", 30];
let coordinate: [number, number, number] = [10, 20, 30];
```

### Objects and Interfaces
```typescript
// Interface
interface User {
  id: number;
  name: string;
  email: string;
  age?: number; // Optional
}

// Type alias
type Point = {
  x: number;
  y: number;
};

// Readonly properties
interface Config {
  readonly apiUrl: string;
  readonly maxRetries: number;
}
```

---

## 🏗️ Advanced Types

### Union and Intersection
```typescript
// Union - either/or
type StringOrNumber = string | number;
type Status = "pending" | "approved" | "rejected";

// Intersection - both/and
type Employee = User & {
  employeeId: string;
  department: string;
};
```

### Generics
```typescript
// Generic function
function identity<T>(arg: T): T {
  return arg;
}

// Generic interface
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

// Generic constraints
function getLength<T extends { length: number }>(arg: T): number {
  return arg.length;
}
```

### Utility Types
```typescript
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}

// Partial - all properties optional
type PartialUser = Partial<User>;

// Required - all properties required
type RequiredUser = Required<User>;

// Pick - select specific properties
type UserPreview = Pick<User, "id" | "name">;

// Omit - exclude specific properties
type PublicUser = Omit<User, "password">;

// Record - create object type
type UserRoles = Record<string, "admin" | "user" | "guest">;
```

### Conditional Types
```typescript
type IsString<T> = T extends string ? true : false;

type A = IsString<string>;  // true
type B = IsString<number>;  // false

// Infer
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
```

### Mapped Types
```typescript
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};

type Optional<T> = {
  [P in keyof T]?: T[P];
};
```

---

## 🔧 Type Guards

### typeof Guard
```typescript
function process(value: string | number) {
  if (typeof value === "string") {
    return value.toUpperCase(); // TypeScript knows it's string
  }
  return value.toFixed(2); // TypeScript knows it's number
}
```

### instanceof Guard
```typescript
class Dog {
  bark() { return "Woof!"; }
}

class Cat {
  meow() { return "Meow!"; }
}

function speak(animal: Dog | Cat) {
  if (animal instanceof Dog) {
    return animal.bark();
  }
  return animal.meow();
}
```

### Custom Type Guards
```typescript
interface Fish {
  swim: () => void;
}

interface Bird {
  fly: () => void;
}

function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}

function move(pet: Fish | Bird) {
  if (isFish(pet)) {
    pet.swim();
  } else {
    pet.fly();
  }
}
```

---

## 🏗️ Design Patterns

### Factory Pattern
```typescript
interface Product {
  name: string;
  price: number;
}

class ConcreteProductA implements Product {
  name = "Product A";
  price = 100;
}

class ConcreteProductB implements Product {
  name = "Product B";
  price = 200;
}

function createProduct(type: "A" | "B"): Product {
  switch (type) {
    case "A":
      return new ConcreteProductA();
    case "B":
      return new ConcreteProductB();
  }
}
```

### Observer Pattern
```typescript
type Listener<T> = (data: T) => void;

class EventEmitter<T> {
  private listeners: Listener<T>[] = [];

  subscribe(listener: Listener<T>): () => void {
    this.listeners.push(listener);
    return () => {
      this.listeners = this.listeners.filter(l => l !== listener);
    };
  }

  emit(data: T): void {
    this.listeners.forEach(listener => listener(data));
  }
}
```

### Builder Pattern
```typescript
class QueryBuilder {
  private select: string[] = [];
  private where: string[] = [];
  private orderBy: string = "";

  addSelect(field: string): this {
    this.select.push(field);
    return this;
  }

  addWhere(condition: string): this {
    this.where.push(condition);
    return this;
  }

  setOrderBy(field: string): this {
    this.orderBy = field;
    return this;
  }

  build(): string {
    let query = `SELECT ${this.select.join(", ")} FROM table`;
    if (this.where.length > 0) {
      query += ` WHERE ${this.where.join(" AND ")}`;
    }
    if (this.orderBy) {
      query += ` ORDER BY ${this.orderBy}`;
    }
    return query;
  }
}
```

---

## ⚠️ Common Pitfalls

### Any Type Overuse
```typescript
// BAD - defeats purpose of TypeScript
function process(data: any): any {
  return data;
}

// GOOD - use proper types
function process(data: unknown): string {
  if (typeof data === "string") {
    return data.toUpperCase();
  }
  return String(data);
}
```

### Non-null Assertion
```typescript
// BAD - can cause runtime errors
const element = document.getElementById("app")!;
element.innerHTML = "Hello";

// GOOD - handle null case
const element = document.getElementById("app");
if (element) {
  element.innerHTML = "Hello";
}
```

### Type Assertions
```typescript
// BAD - bypasses type checking
const data = someValue as string;

// GOOD - use type guards
if (typeof someValue === "string") {
  const data = someValue; // TypeScript knows it's string
}
```

### Ignoring strictNullChecks
```typescript
// With strictNullChecks: true
function process(value: string | null) {
  // ERROR: Object is possibly 'null'
  return value.toUpperCase();
}

// Fix
function process(value: string | null) {
  if (value === null) {
    return "";
  }
  return value.toUpperCase();
}
```

---

## 🚀 Performance Tips

### Avoid Unnecessary Type Computations
```typescript
// BAD - recomputed every call
function getData(): ComplexType {
  // Complex type computation
}

// GOOD - computed once
type DataType = ComplexType;
function getData(): DataType {
  // Uses pre-computed type
}
```

### Use const assertions
```typescript
// Type is string[]
const colors = ["red", "green", "blue"];

// Type is readonly ["red", "green", "blue"]
const colors = ["red", "green", "blue"] as const;
```

### Discriminated Unions
```typescript
// Efficient pattern matching
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "rectangle"; width: number; height: number }
  | { kind: "triangle"; base: number; height: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "rectangle":
      return shape.width * shape.height;
    case "triangle":
      return (shape.base * shape.height) / 2;
  }
}
```

---

## 🧪 Testing Best Practices

### Type-Safe Mocks
```typescript
interface UserService {
  getUser(id: number): Promise<User>;
  createUser(data: Partial<User>): Promise<User>;
}

// Type-safe mock
const mockUserService: UserService = {
  getUser: jest.fn().mockResolvedValue({ id: 1, name: "John" }),
  createUser: jest.fn().mockResolvedValue({ id: 2, name: "Jane" }),
};
```

### Testing Generics
```typescript
describe("Stack", () => {
  it("should work with numbers", () => {
    const stack = new Stack<number>();
    stack.push(1);
    expect(stack.pop()).toBe(1);
  });

  it("should work with strings", () => {
    const stack = new Stack<string>();
    stack.push("hello");
    expect(stack.pop()).toBe("hello");
  });
});
```

---

## 📚 Quick Reference

### Declaration Files
```typescript
// ambient.d.ts
declare module "*.svg" {
  const content: string;
  export default content;
}

declare global {
  interface Window {
    myCustomProperty: string;
  }
}
```

### Module Systems
```typescript
// ES Modules (preferred)
import { User } from "./models";
export { UserService };

// CommonJS (legacy)
const { User } = require("./models");
module.exports = { UserService };
```

### tsconfig.json Essentials
```json
{
  "compilerOptions": {
    "strict": true,
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "node",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  }
}
```

---

**Knowledge Version**: 1.0  
**Last Updated**: March 2026