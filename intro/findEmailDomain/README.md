An email address such as `"John.Smith@example.com"` is made up of a local part (`"John.Smith"`), an `"@"` symbol, then a domain part (`"example.com"`).

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters.

Given a valid email address, find its domain part.

**Example**

* For `address = "prettyandsimple@example.com"`, the output should be
`findEmailDomain(address) = "example.com"`;

* For `address = "fully-qualified-domain@codesignal.com"`, the output should be
`findEmailDomain(address) = "codesignal.com"`.
