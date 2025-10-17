from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="NIH Grant Assistant API")

class GrantDocument(BaseModel):
    document: str

@app.post("/parse-grant-sections")
def parse_grant_sections(payload: GrantDocument):
    return {"sections": ["Specific Aims", "Research Strategy", "Abstract"]}

class ParsedSections(BaseModel):
    parsed_sections: List[str]

@app.post("/run-compliance-check")
def run_compliance_check(payload: ParsedSections):
    return {"compliance": "All sections meet NIH SF424 guidelines."}

class ReviewerFeedbackInput(BaseModel):
    document: str
    review_focus: Optional[str] = None

@app.post("/generate-reviewer-feedback")
def generate_reviewer_feedback(payload: ReviewerFeedbackInput):
    return {"feedback": f"Feedback for focus: {payload.review_focus or 'Full Review'}"}

class RevisionRequest(BaseModel):
    original_text: str
    feedback: str

@app.post("/revise-based-on-feedback")
def revise_based_on_feedback(payload: RevisionRequest):
    return {"revised_text": "This is your revised text based on the feedback."}

class RewriteRequest(BaseModel):
    text: str
    emphasis: Optional[str] = None

@app.post("/nih-style-rewrite")
def nih_style_rewrite(payload: RewriteRequest):
    return {"rewritten": f"Rewritten in NIH tone with emphasis on {payload.emphasis or 'Clarity'}."}

class SectionText(BaseModel):
    section_text: str

@app.post("/analyze-page-limits")
def analyze_page_limits(payload: SectionText):
    return {"estimated_pages": 1.5, "over_limit": False}

class ExportReviewRequest(BaseModel):
    review_summary: str
    file_format: Optional[str] = "docx"

@app.post("/export-review-report")
def export_review_report(payload: ExportReviewRequest):
    return {"file_url": f"https://your-server.com/reports/output.{payload.file_format}"}

class RevisionHistory(BaseModel):
    revision_summary: str

@app.post("/track-revision-history")
def track_revision_history(payload: RevisionHistory):
    return {"status": "Revision recorded."}
