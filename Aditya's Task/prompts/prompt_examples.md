# Example Prompt & Response

**Prompt:**
Analyze the following clause for ADGM compliance:
"All disputes shall be settled by UAE Federal Courts."

**Expected Response:**
```json
{
  "compliant": false,
  "issue": "Jurisdiction references UAE Federal Courts instead of ADGM Courts",
  "suggestion": "Replace with 'All disputes shall be settled by ADGM Courts.'",
  "reference_snippet": "ADGM Companies Regulations 2020, Art. 6..."
}
