# Security Policy

NOAA-Spec is a local data-cleaning package and command-line tool for NOAA ISD /
Global Hourly files. It is not a network service and does not run a server,
accept remote requests, or manage credentials.

## Reporting A Security Issue

If you believe you have found a security issue, please report it responsibly:

- Open a GitHub issue if the report does not expose sensitive data, private
  infrastructure details, or a working exploit.
- If the report contains sensitive details, contact the maintainer using the
  contact information published with the repository metadata instead of posting
  the full details publicly.

Please include:

- affected NOAA-Spec version or commit;
- operating system and Python version;
- the command or API call involved;
- a minimal reproduction, using synthetic or public data when possible;
- whether the issue can cause code execution, file overwrite, data disclosure,
  or incorrect scientific output.

## Disclosure Guidance

Give the maintainer reasonable time to investigate before publicizing sensitive
details. For data-cleaning correctness issues that do not create a security
risk, use the normal issue tracker and label the report as a bug or
documentation issue.
