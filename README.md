# Hello, GitHub!

A growing collection of small programs that say:

```text
Hello, GitHub!
```

The repository currently contains **90 programming languages**, spanning systems programming, scripting, functional programming, scientific computing, hardware description, smart contracts, and several historical languages.

> There is no finite, universally accepted list of every programming language. New languages and dialects appear continuously, so this project favors a broad, verifiable catalog that can keep growing.

## Browse the collection

Every example lives in `src/<language>/` and is listed in [`languages.json`](languages.json). The catalog includes:

- **Systems and native:** C, C++, Rust, Zig, D, V, Nim, Ada, Assembly, Objective-C, CUDA, and OpenCL
- **JVM and managed:** Java, Kotlin, Scala, Groovy, C#, F#, and Visual Basic .NET
- **Web and scripting:** JavaScript, TypeScript, Python, Ruby, PHP, Perl, Raku, Lua, Bash, PowerShell, Fish, Nushell, and more
- **Functional:** Haskell, Elm, Erlang, Elixir, Clojure, Common Lisp, Scheme, Racket, OCaml, Standard ML, PureScript, Reason, Idris, and Gleam
- **Scientific and data:** R, Julia, MATLAB, Wolfram Language, Fortran, Chapel, and SQL
- **Hardware and contracts:** Verilog, SystemVerilog, VHDL, Solidity, and Q#
- **Classic and specialist:** COBOL, Pascal, Forth, Smalltalk, Prolog, XQuery, XSLT, Ballerina, Pony, and others

## Validate the collection

The validator checks that the manifest is well formed, every entry points to a unique non-empty source file, and every example contains the exact greeting.

```bash
make test
```

## Add another language

1. Create `src/<language>/hello.<extension>` with a program that outputs `Hello, GitHub!`.
2. Add its display name and source path to `languages.json` in alphabetical order.
3. Run `make test`.

Contributions for additional languages and dialects are welcome.
